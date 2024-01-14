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
    from sqlalchemy.orm import sessionmaker  # To create 'session' manager.
    from model_state import Base, State  # To access the table 'states'.

    if len(argv) != 4:
        print(__doc__)
        exit(1)

    user, pw, db = argv[1], argv[2], argv[3]  # Spread argv into variables.
    engine = create_engine(  # Connecting to database.
       f"mysql+mysqldb://{user}:{pw}@localhost:3306/{db}",  # Connection string.
       pool_pre_ping=True)  # Test connections before handing them out.

    Base.metadata.create_all(engine)  # Create metadata and tables.

    Session = sessionmaker(  # Starting a db access session.
         bind=engine,  # Select the engine to be used for the session.
         expire_on_commit=True,  # Objects reloaded after every commit.
         autoflush=True,  # Sync with database on every query.
         autocommit=True)  # Every query is a transaction.

    session = Session()  # Create a Session instance.

    stmt = (  # Create a statement to query the database.
            session.query(State)  # Select all states.
            .order_by(State.id.asc()))  # Order by id in ascending order.
    states = stmt.all()  # Execute the statement and save the result.

    for state in states:  # Iterate over the result.
        print(f"{state.id}: {state.name}")  # Print the result.

    session.close()  # Close the session.
    # session.commit(), session.expunge() are not needed due to configs.
