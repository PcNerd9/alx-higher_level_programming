#!/usr/bin/python3
"""
State class inheriting from sqlalchemy base
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    State class mapping to the state class
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
