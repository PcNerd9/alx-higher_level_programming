#!/usr/bin/python3

"""
create a state and city from the database
"""

from sys import argv
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker


def main():
    """The entry to the main program
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Francisco")
    new_state = State(name="California")
    new_state.cities.append(new_city)

    session.add(new_state)
    session.add(new_city)

    session.commit()


if __name__ == "__main__":
    main()
