import os
from datetime import datetime, timedelta
from typing import Optional

import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models.telephony import ExecutiveDidMap

# 🟢 Require secret, no unsafe defaults
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET environment variable must be set")

JWT_ALG = os.getenv("JWT_ALG", "HS256")
JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", "5"))  # default 5min if not set


def find_mapping(session: Session, did: str) -> Optional[ExecutiveDidMap]:
    stmt = select(ExecutiveDidMap).where(ExecutiveDidMap.did == did)
    return session.execute(stmt).scalars().first()


def resolve_did(did: str) -> dict:
    """Resolve a DID to its mapping, returning a signed JWT token."""
    with SessionLocal() as session:
        mapping = find_mapping(session, did)
        if not mapping:
            return {"ok": False, "error": "DID not mapped"}

        try:
            payload = {
                "did": mapping.did,
                "persona": mapping.persona,
                "cnam": mapping.cnam,
                "iat": int(datetime.utcnow().timestamp()),
                "exp": int((datetime.utcnow() + timedelta(minutes=JWT_EXP_MINUTES)).timestamp()),
            }
            token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
            return {
                "ok": True,
                "persona": mapping.persona,
                "cnam": mapping.cnam,
                "token": token,
            }
        except Exception as e:
            return {"ok": False, "error": f"Token generation failed: {str(e)}"}


def upsert_mapping(session: Session, did: str, persona: str, cnam: str) -> ExecutiveDidMap:
    """Insert or update a DID mapping."""
    mapping = find_mapping(session, did)
    if mapping:
        mapping.persona = persona
        mapping.cnam = cnam
    else:
        mapping = ExecutiveDidMap(did=did, persona=persona, cnam=cnam)
        session.add(mapping)
    session.commit()
    session.refresh(mapping)
    return mapping


def delete_mapping(session: Session, did: str) -> bool:
    """Delete a DID mapping if it exists."""
    mapping = find_mapping(session, did)
    if not mapping:
        return False
    session.delete(mapping)
    session.commit()
    return True
