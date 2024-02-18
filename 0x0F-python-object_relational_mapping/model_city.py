#!/usr/bin/python3

"""
create a new model cities into the hbtn_0e_6_usa
"""


from sqlalchemy import create_engine, Column, String, Integer, Foreignkey
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    

