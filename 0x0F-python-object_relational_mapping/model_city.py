#!/usr/bin/python3

"""
Create the city class database
"""

from sqlalchemy import ForeignKey
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class : Cities

    Attribute:
        id (int)
        name (int)
        state_id (int)
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
