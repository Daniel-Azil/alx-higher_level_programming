#!/usr/bin/python3
"""
    A script that creates the City table in db
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """
        A class that inherits from Base defined in relationship.state module
    """
    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey=("states.id"), nullable=False)
