#!/usr/bin/python3

"""
    A script that lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
import sqlalchemy.orm
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    database_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                    format(user, passwd, database),
                                    pool_pre_ping=True)

    Base.metadate.create_all(database_engine)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    record = session.query(State).filter(State.name.ilike("%a%")) \
                    .order_by(State.id).all()

    for names in record:
        print("{}: {}". format(names.id, names.name))

    session.close()
