from datetime import datetime
from app.database import Base
from sqlalchemy import ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped

class Transactions(Base):
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    transaction_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    transaction_sum: Mapped[float] = mapped_column(Float, nullable=False)
    comment: Mapped[str] = mapped_column(String)
