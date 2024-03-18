#!/usr/bin/python3

"""
delete a state object from the hbtn_0e_6_usa
"""


def main():
    """
    the entry to the main program
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    states = session.query(State).filter(State.name.like("%a%")).delete(
            synchronize_session=False)
    session.commit()


if __name__ == "__main__":
    main()
