import os
from datetime import datetime, timedelta
from typing import Optional

import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..models.telephony import ExecutiveDidMap

JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
JWT_ALG = "HS256"


def find_mapping(session: Session, did: str) -> Optional[ExecutiveDidMap]:
    stmt = select(ExecutiveDidMap).where(ExecutiveDidMap.did == did)
    return session.execute(stmt).scalars().first()


def resolve_did(did: str) -> dict:
    with SessionLocal() as session:
        mapping = find_mapping(session, did)
        if not mapping:
            return {"ok": False, "error": "DID not mapped"}

        payload = {
            "did": mapping.did,
            "persona": mapping.persona,
            "cnam": mapping.cnam,
            "iat": int(datetime.utcnow().timestamp()),
            "exp": int((datetime.utcnow() + timedelta(minutes=5)).timestamp()),
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
        return {"ok": True, "persona": mapping.persona, "cnam": mapping.cnam, "token": token}

