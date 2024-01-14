#!/usr/bin/python3

"""
Prints State object with name passed as argument from the hbtn_0e_6_usa db.

Usage: ./test.py <mysql username> <mysql password> <database name> <state name>

Arguments:
    mysql username: username to connect the mySQL
    mysql password: password to connect the mySQL
    database name: name of the database
    state name: name of the state to search
"""
from sys import argv  # To collect user input
from model_state import Base, State  # To access the State class
from sqlalchemy import create_engine  # To connect to the db
from sqlalchemy.orm import Session  # To communicate with the db


if __name__ == "__main__":  # Execute only if run as a script
    user, pw, db, state = argv[1:]  # Unpack the arguments
    engine = create_engine(  # Connect to the db
        f"mysql+mysqldb://{user}:{pw}@localhost/{db}",  # URI
        pool_pre_ping=True)  # Test connections before handing them out
    Base.metadata.create_all(engine)  # Create metadata tables in db
    sess = Session(engine)  # Instantiate Session class

    found = False  # Flag to indicate if the state was found
    # Query the db for the State object with the name passed as argument
    for state in (
            sess.query(State).filter(State.name == state).order_by(State.id)):
        if state:
            print(f"{state.id}")  # Print the state id
            found = True  # Set a flag to indicate the state was found
            break
    if not found:  # If the state doesn't exist
        print("Not found")  # Print an error message
    sess.close()  # Close the connection to the db
