#!/usr/bin/python3

"""
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State
from sys import argv


def main():
    """
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    results = session.query(State, City).order_by(City.id).filter(
            State.id == City.state_id)
    for result in results:
        print("{}: ({}) {}".format(result.State.name, result.City.id,
                                   result.City.name))


if __name__ == "__main__":
    main()
