#!/usr/bin/python3

"""
Defines Class City that inherits from Base, a declarative base from SQLAlchemy.

Attributes:
-----------
    id (int): The id of the city.
    name (str): The name of the city.
    state_id (int): The id of the state that the city is in.
"""

from sqlalchemy import Column, Integer, String, ForeignKey  # For db ops
from relationship_state import Base, State  # For declarative base and state


class City(Base):
    """
    Represents a city for a MySQL database.

    This class maps to the table 'cities' in the MySQL database 'hbtn_0e_6_usa'

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        id (sqlalchemy.Integer): The city's id.
        name (sqlalchemy.String): The city's name.
        state_id (sqlalchemy.Integer): The state's id that the city is in.
    """
    __tablename__ = "cities"  # The name of the MySQL table to store Cities.
    id = Column(Integer, primary_key=True, autoincrement=True)  # The city's id
    name = Column(String(128), nullable=False)  # The city's name
    # The id of the city's state, must be an existing state id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
