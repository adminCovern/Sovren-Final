from sqlalchemy import Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base

class ExecutiveDidMap(Base):
    __tablename__ = "executive_did_map"
    __table_args__ = (
        UniqueConstraint("did", name="uq_executive_did_map_did"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    did: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    persona: Mapped[str] = mapped_column(String(64), nullable=False)
    cnam: Mapped[str] = mapped_column(String(64), nullable=False)

