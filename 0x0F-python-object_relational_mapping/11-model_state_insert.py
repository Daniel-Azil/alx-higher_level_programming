#!/usr/bin/python3

"""
    A script that adds the State object “Louisiana” to
    the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    database_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                    format(user, passwd, database),
                                    pool_pre_ping=True)

    Base.metadata.create_all(database_engine)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    new_record = State(name="Louisiana")
    session.add(new_record)
    session.commit()

    new_record = session.query(State).filter(State.name=="Louisiana").one()
    print(new_record.id)

    session.close()
