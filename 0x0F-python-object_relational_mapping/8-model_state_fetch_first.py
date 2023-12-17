#!/usr/bin/python3

""" A script that prints the first State object
    from the database hbtn_0e_6_usa
"""

import sqlalchemy
from model_state import Base, State
import sqlalchemy.orm
import sys

if __name__ == "__main__":

    database_engine = sqlalchemy.create_engine("""mysql+mysqldb://{}:
                                               {}@localhost:3306/{}""".
                                               format(sys.argv[1], sys.argv[2],
                                                      sys.argv[3]),
                                               pool_pre_ping=True)

    Base.metadata.create_all(database_engine)
    Session = sqlalchemy.orm.sessionmaker(database_engine)
    session = Session()
    records = session.query(State).order_by(State.id).first()

    if records:
        print("{}: {}".format(records.id, records.name))
    else:
        print("Nothing")

    session.close()
