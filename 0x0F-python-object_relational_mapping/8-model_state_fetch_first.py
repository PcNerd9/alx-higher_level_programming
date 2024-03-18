#!/usr/bin/python3

"""
using the sqlalchemy to query the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys


def main():
    """
    The main entry of the program
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()
    if (first_state):
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
