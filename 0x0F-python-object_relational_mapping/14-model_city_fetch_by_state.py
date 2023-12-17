#!/usr/bin/python3

"""
    A  script 14-model_city_fetch_by_state.py that prints
    all City objects from the database hbtn_0e_14_usa
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    user = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]

    database_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                                    format(user, passwd, database_name),
                                    pool_pre_ping=True)
    Session = sessionmaker(bind=database_engine)
    Base.metadata.create_all(database_engine)

    session = Session()

    for q in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(q[0], q[1], q[2]))

    session.close()
