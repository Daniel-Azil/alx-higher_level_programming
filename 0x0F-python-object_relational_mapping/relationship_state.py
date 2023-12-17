#!/usr/bin/python3
"""
    A script containingc that creates states table with given records
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

mydata = MetaData()
Base = declarative_base(metadata=mydata)


class State(Base):
    """
    A class that creates states table with given records
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
