#!/usr/bin/python3
"""
    A script that creates the City table in db
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mydata = MetaData()
Base = declarative_base(mymetadata=mydata)


class State(Base):
    """
        A class that creates the table name state and it record name
    """

    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
