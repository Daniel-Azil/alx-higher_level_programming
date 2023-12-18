#!/usr/bin/python3
""" A script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state_record in session.query(State).order_by(State.id):
        for city_rel in state_record.cities:
            print(city_rel.id, city_rel.name, sep=": ", end="")
            print(" -> " + state_record.name)

    session.close()
