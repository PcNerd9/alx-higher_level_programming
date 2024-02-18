#!/usr/bin/python3

"""
Add a new row to the hbtn_0e_6_usa database
using sqlalchemy
"""


def main():
    """
    The main entry to the program
    """
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    main()
