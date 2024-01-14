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

if __name__ == "__main__":  # Execute only if run as a script
    from sys import argv, exit  # To collect user input and handle errors
    from model_state import Base, State  # To access the State class
    from sqlalchemy import create_engine  # To connect to the db
    from sqlalchemy.orm import sessionmaker  # To communicate with the db

    user, pw, db, state = argv[1:]  # Unpack the arguments
    engine = create_engine(  # Connect to the db
        "mysql+mysqldb://{user}:{pw}@localhost/{db}",  # URI
        pool_pre_ping=True)  # Test connections before handing them out
    Base.metadata.create_all(engine)  # Create metadata tables in db
    Session = sessionmaker(bind=engine)  # Create Session class
    session = Session()  # Instantiate Session class

    # Query the db for the State object with the name passed as argument
    state = session.query(State).filter(State.name == state).first()
    if state:  # If the state exists
        print(state.id)  # Print the state id
    else:  # If the state doesn't exist
        print("Not found")  # Print an error message

    session.close()  # Close the connection to the db
