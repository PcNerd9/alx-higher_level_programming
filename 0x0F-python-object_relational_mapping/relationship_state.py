#!/usr/bin/python3

"""
State class inheriting from sqlalchemy base
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """
    State class mapping to the states table
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(60), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
