#!/usr/bin/python3

"""
Show all the states in the database that contain the letter a.

Usage: ./test.py <username> <password> <database name>

Args:
    username - username to connect the mySQL
    password - password to connect the mySQL
    database - Name of the database
"""

if __name__ == "__main__":  # Import guard
    from sys import argv, exit  # For terminal arguments and error handling
    from sqlalchemy.orm import Session  # To create a session manager
    from sqlalchemy import create_engine  # To create a connection to the DB
    from model_state import Base, State  # Objects being managed by db

    if len(argv) != 4:  # Check for correct number of arguments
        print(__doc__)  # Print the documentation
        exit(1)  # Exit with error

    user, pw, db = argv[1:]  # Spreading argv into variables.

    engine = create_engine(
            f"mysql+mysqldb://{usr}:{pw}@localhost:3306/{db}",
            pool_pre_ping=True)  # Check connections before passing them

    Base.metadata.create_all(engine)  # Create tables for declared objects
    session = Session(engine)  # Starting a db access session

    states = session.query(State).\
        filter(State.name.like("%a%")).\
        order_by(State.id)  # Order by id

    for state in states:  # Print all the states
        print(f"{state.id}: {state.name}")
    session.close()  # Close the session
