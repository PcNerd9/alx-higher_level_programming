#!/usr/bin/python3

"""
query the database to fetch all the states
that has letter a in it using sqlalchemy
"""


def main():
    """
    The entry of the main program
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)

    states = session.query(State).filter_by(State.name="%a%").order_by(States.id)
    for state in states:
        print(f"{state.id}: {state.name}")
