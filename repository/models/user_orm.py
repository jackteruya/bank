from sqlalchemy import Column, String, Integer

from repository.models.db_base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    nationality = Column(String(32), nullable=False)
    password = Column(String(64), nullable=False)
