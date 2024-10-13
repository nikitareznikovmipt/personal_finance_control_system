from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy.types import Enum
from enum import Enum as PyEnum

class UserRole(PyEnum):
    USER = "user"
    ADMIN = "admin"

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.USER, nullable=False)
