from sqlalchemy import Column, Integer, String, DateTime, Float

from repository.models.db_base import Base


class Statement(Base):
    __tablename__ = "statement"

    id = Column(Integer, primary_key=True)
    account_number = Column(Integer, nullable=False)
    date = Column(DateTime)
    value = Column(Float(precision=2))
    operation = Column(String(1))
