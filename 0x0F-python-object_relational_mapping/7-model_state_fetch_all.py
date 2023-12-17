#!/usr/bin/python3

""" script that lists all State objects from the database hbtn_0e_6_usa"""

import sqlalchemy
import sys
from model_state import Base, State
import sqlalchemy.orm

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = sqlalchemy.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                                    format(user, passwd, db), pool_pre_ping=True)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()

    for records in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(records.id, records.name))
    session.close()
