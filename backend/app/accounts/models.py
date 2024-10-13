from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float, ARRAY, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped

class Accounts(Base):
    __tablename__ = 'accounts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    default_flag: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    aliasis: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    initial_value: Mapped[int] = mapped_column(Integer, nullable=False)
    # TODO: добавить limit, limit_period и валюту
    active_flag: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
