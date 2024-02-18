#!/usr/bin/python3

"""
update the state object from the hbtn_0e_6_usa
"""


def main():
    """
    entry to the main program
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.arv[2], sys.argv[3]),
                           pre_pool_ping=True)
    session = Session(engine)
    state = session.query(State).filter_by(State.id=2).first()
    state.name = "New Mexico"
    session.commit()


if __name__ == "__main__":
    main()
