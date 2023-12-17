#!/usr/bin/python3

"""
    A script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    database_name = sys.argv[3]

    database_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                    format(user, passwd, database_name),
                                    pool_pre_ping=True)
    Session = sessionmaker(bind=database_engine)

    Base.metadata.create_all(database_engine)

    session = Session()

    record_id = session.query(State).filter(State.id == 2).first()
    record_id.name = 'New Mexico'
    session.commit()

    session.close()
