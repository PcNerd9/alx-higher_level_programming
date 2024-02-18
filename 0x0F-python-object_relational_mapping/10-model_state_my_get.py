#!/usr/bin/python3

"""
query the states table for hbtn_0e_6_usa database
using sqlalchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

def main():
    """
    The entry of the main program
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    state = session.query(State).filter_by(name="Texas").order_by(State.id)
    if (state):
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
