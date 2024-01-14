#!/usr/bin/python3

"""
Creates State "California" with City "San Francisco" from hbtn_0e_100_usa db

Usage: ./<file name> <mysql username> <mysql password> <database name>

Arguments:
    mysql username: username to connect the mySQL
    mysql password: password to connect the mySQL
    database name: name of the database
"""


if __name__ == "__main__":  # Execute only if run as a script
    from sys import argv, exit  # To collect user input and exit
    from relationship_city import Base, State, City
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

    # Create a new State object with existing City object
    sess.add(State(name="California", cities=[City(name="San Francisco")]))
    sess.commit()  # Save changes to db
    sess.close()  # Close the connection
