#!/usr/bin/python3

"""
Query the database to list all the states
and cities in the database
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from relationship_state import State, Base
from relationship_city import City


def main():
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).all()
    for obj in result:
        print("{}: {}".format(obj.id, obj.name))
        for city in obj.cities:
            print("\t{}: {}".format(city.id, city.name))


if __name__ == "__main__":
    main()
