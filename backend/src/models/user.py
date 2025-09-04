from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base

class User(Base):
    __tablename__ = "users"

    # Surrogate PK, auto-increment
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Email must be unique for login
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    # Optional display name
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    # User activation flag
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
