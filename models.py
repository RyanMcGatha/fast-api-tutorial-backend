from sqlalchemy import Column, Integer, String
from database import Base

class CEO(Base):
    __tablename__ = "ceos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    company = Column(String)
