from sqlalchemy import Column, Integer, String, DateTime, Float

from repository.models.db_base import Base


class Account(Base):
    __tablename__ = "account"

    account = Column(Integer, primary_key=True)
    cpf = Column(String(11), nullable=False)
    created_date = Column(DateTime)
    bank_balance = Column(Float(precision=2))
