#!/usr/bin/python3

from sqlalchemy import Column, String, create_engine, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


engine = create_engine("mysql+mysqldb://pcnerd:Allsum Gye9@localhost/hbtn_0e_100_usa", pool_pre_ping=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

new_state = State(name="California")
new_city = City(name="San Francisco")
new_state.cities.append(new_city)

session.add(new_state)
session.add(new_city)
session.commit()
session.close()
