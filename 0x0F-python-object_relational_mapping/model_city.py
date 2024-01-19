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

    __tablename__ = "cities"  # MySQL table name
    id = Column(  # MySQL id column
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
    )
    name = Column(String(128), nullable=False)  # MySQL name column
    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False,
    )
