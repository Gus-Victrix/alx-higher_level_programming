#!/usr/bin/python3

"""
Define Class State that inherits from Base, a declarative base from SQLAlchemy.
It also shows the relationship between this class and the City class.

Attributes:
-----------
    id (int): The id of the state.
    name (str): The name of the state.
    cities (sqlalchemy.orm.relationship): The state's cities.
"""

from sqlalchemy.orm import relationship  # For creating relationships
from sqlalchemy import Column, Integer, String  # For db ops
from sqlalchemy.ext.declarative import declarative_base  # For base class

Base = declarative_base()  # Create a declarative base class


class State(Base):
    """
    Represents a state for a MySQL database.

    This class maps to the table 'states' in the MySQL database 'hbtn_0e_6_usa'

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): The state's id.
        name (sqlalchemy.String): The state's name.
        cities (sqlalchemy.orm.relationship): The state's cities.
    """
    __tablename__ = "states"  # The name of the MySQL table to store Cities.
    id = Column(Integer, primary_key=True)  # The city's id
    name = Column(String(128), nullable=False)  # The city's name
    cities = relationship("City", backref="state") # The state's cities
