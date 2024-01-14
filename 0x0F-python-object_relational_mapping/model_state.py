#!/usr/bin/python3

"""
Defines State class which inherits from Base.

Base is a declarative base created by SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String  # For creating typed columns
from sqlalchemy.ext.declarative import declarative_base
# Making it possible to create classes that SQLAlchemy can manage.

Base = declarative_base()  # SQLAlchemy managable class.


class State(Base):  # State class inherits from Base.
    """
    Defines State class which inherits from Base.

    Attributes:
        __tablename__ (str): Name of the table.
        id (int): State id.
        name (str): State name.
    """
    __tablename__ = 'states'  # Necessity for SQLAlchemy to work.
    id = Column(  # Creating a column named id in the table.
            Integer,  # Type of data that goes into the column.
            primary_key=True,  # This will enforce uniqueness of column items.
            unique=True,  # This will enforce uniqueness of column items.
            autoincrement=True,  # The alchemy does the allocation job.
            nullable=False)  # Ensures that the column is not empty.
    name = Column(  # Creating a column named name in the table.
            String(128),  # Column datatype and length specification.
            nullable=False)  # Ensures that the column is not empty.
