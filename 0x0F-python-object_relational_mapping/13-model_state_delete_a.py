#!/usr/bin/python3

"""
    script that deletes all State objects with a name
    containing the letter a
    from the database hbtn_0e_6_usa
"""

import sys
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

    # extract record_name_match with a in them
    record_name_match = session.query(State). \
        filter(State.name.ilike('%a%')).all()

    for record in record_name_match:
        session.delete(record)

    session.commit()

    session.close()
