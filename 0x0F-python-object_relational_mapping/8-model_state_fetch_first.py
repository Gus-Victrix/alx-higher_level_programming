#!/usr/bin/python3

"""
Display first State object from the database hbtn_0e_6_usa

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

    user, pw, db = argv[1:]  # Spread argv into variables.

    engine = create_engine(  # Connecting to database.
       f"mysql+mysqldb://{user}:{pw}@localhost:3306/{db}",  # Connecting to db.
       pool_pre_ping=True)  # Test connections before handing them out.

    Base.metadata.create_all(engine)  # Create metadata and tables.

    session = Session(engine)  # Create a Session instance bound to engine.
    state = session.query(State).order_by(State.id).first()  # Query the db.
    if state:  # If the query returned a result.
        print(f"{state.id}: {state.name}")
    else:  # If the query returned nothing.
        print("Nothing")
    session.close()  # Close the session.
    # session.commit(), session.expunge() are not needed due to configs.
