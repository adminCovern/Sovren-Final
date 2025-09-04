from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base

class ExecutiveDidMap(Base):
    __tablename__ = "executive_did_map"

    # Surrogate primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # DID is unique and indexed for fast lookups
    did: Mapped[str] = mapped_column(String(32), nullable=False, unique=True, index=True)

    # Persona and CNAM (caller name) values
    persona: Mapped[str] = mapped_column(String(128), nullable=False)
    cnam: Mapped[str] = mapped_column(String(128), nullable=False)
