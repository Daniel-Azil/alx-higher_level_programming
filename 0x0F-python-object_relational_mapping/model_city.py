#!/usr/bin/python3

"""
    A script that contains creates the records of table named cities.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model_state import Base, State


Base = declarative_base()


class City(Base):
    """
        A class defines that defines the given records.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
