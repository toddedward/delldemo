from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Color(Base):
    __tablename__ = "colors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)


class Memory(Base):
    __tablename__ = "memory"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Integer)



class Laptop(Base):
    __tablename__ = "laptop"
    
    id = Column(Integer, primary_key=True, index=True)
    color = Column(String, unique=True, index=True)
    memory = Column(String, unique=True, index=True)
    price = Column(Integer)


