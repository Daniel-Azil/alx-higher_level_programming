#!/usr/bin/python3

""" A script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import State, Base


if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    cmd_arg = sys.argv[4]

    database_engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                                    format(user, passwd, database),
                                    pool_pre_ping=True)

    Base.metadata.create_all(database_engine)
    Session = sessionmaker(bind=database_engine)

    session = Session()

    record = session.query(State).filter(State.name == cmd_arg).one_or_none()

    if record is None:
        print("Not found")
    else:
        print(record.id)

    session.close()
