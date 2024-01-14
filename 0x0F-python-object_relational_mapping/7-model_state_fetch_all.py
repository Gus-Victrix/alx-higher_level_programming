#!/usr/bin/python3

"""
Lists all State objects from the database hbtn_0e_6_usa

Usage: ./test.py <username> <password> <database name>

Args:
    username - username to connect the mySQL
    password - password to connect the mySQL
    database - Name of the database
"""

if __name__ == "__main__":  # Import guard.
    from sys import argv, exit  # For CLI arguments and error handling.
    from sqlalchemy import create_engine  # To connect to the database.
    from sqlalchemy.orm import Session  # To handle sessions.
    from model_state import Base, State  # To access the table 'states'.

    if len(argv) != 4:
        print(__doc__)
        exit(1)

    user, pw, db = argv[1], argv[2], argv[3]  # Spread argv into variables.
    engine = create_engine(  # Connecting to database.
       f"mysql+mysqldb://{user}:{pw}@localhost:3306/{db}",  # Connecting to db.
       pool_pre_ping=True)  # Test connections before handing them out.

    Base.metadata.create_all(engine)  # Create metadata and tables.

    session = Session(engine)  # Create a Session instance bound to engine.
    states = session.query(State).order_by(State.id)  # Query the table.
    for state in states:  # Iterate over the result.
        print(f"{state.id}: {state.name}")  # Print the result.

    session.close()  # Close the session.
    # session.commit(), session.expunge() are not needed due to configs.
