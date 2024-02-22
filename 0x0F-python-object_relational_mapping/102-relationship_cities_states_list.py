#!/usr/bin/python3

"""
query the database to get all the cities in a state
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
from sys import argv


def main():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).all()
    for obj in result:
        print("{}: {} -> {}".format(obj.id, obj.name, obj.state.name))


if __name__ == "__main__":
    main()
