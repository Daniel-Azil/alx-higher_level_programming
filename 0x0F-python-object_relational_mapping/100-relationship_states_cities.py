#!/usr/bin/python3
"""
    script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    database_name = argv[3]
    database_engines = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                     format(user, passwd, database_name),
                                     pool_pre_ping=True)
    Base.metadata.create_all(database_engines)
    Session = sessionmaker(bind=database_engines)
    session = Session()

    # create state "California" with city attribute "San Francisco"
    state_value = State(name="California")
    city_value = City(name="San Francisco")
    state_value.cities.append(city_value)

    session.add(state_value)
    session.add(city_value)

    session.commit()
    session.close()
