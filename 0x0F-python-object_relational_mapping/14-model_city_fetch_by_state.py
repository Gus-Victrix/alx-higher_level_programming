#!/usr/bin/python3

"""
Prints all city ojects from the database hbtn_0e_14_usa

Usage: ./<file name> <mysql username> <mysql password> <database name>

Arguments:
    mysql username: username to connect the mySQL
    mysql password: password to connect the mySQL
    database name: name of the database
"""


if __name__ == "__main__":  # Execute only if run as a script
    from sys import argv, exit  # To collect user input and exit
    from model_city import Base, State, City  # To access the State class
    from sqlalchemy import create_engine  # To connect to the db
    from sqlalchemy.orm import Session  # To communicate with the db

    if len(argv) != 4:  # If the number of arguments is not 4
        print(__doc__)  # Print the documentation
        exit(1)
    user, pw, db = argv[1:]  # Unpack the arguments
    engine = create_engine(  # Connect to the db
        f"mysql+mysqldb://{user}:{pw}@localhost:3306/{db}",  # URI
        pool_pre_ping=True)  # Test connections before handing them out
    Base.metadata.create_all(engine)  # Create metadata tables in db
    sess = Session(engine)  # Instantiate Session class

    # Fetch all City objects from the db and print them joined with State
    rows = sess.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()

    for state, city in rows:
        print(f"{state.name}: ({city.id}) {city.name}")

    sess.close()
