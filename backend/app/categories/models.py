from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float, ARRAY, Boolean
from sqlalchemy.orm import relationship, mapped_column, Mapped

class Categories(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    aliasis: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    # TODO: добавить limit и limit_period
    active_flag: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
