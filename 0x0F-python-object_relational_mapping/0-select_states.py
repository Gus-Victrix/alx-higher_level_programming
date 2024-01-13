#!/usr/bin/env python3

"""
Lists all states from the database hbtn_0e_0_usa

Usage: ./<filename> <username> <password> <database_name>

Args:
    user_name (argv[1]): The username of the database to be used.
    password (argv[2]): User password.
    database (argv[3]): Database name.
"""


if __name__ == "__main__":
    import sys  # For accessing commandline arguements.
    import MySQLdb as ms  # For accessing the MySQL database.

    if len(sys.argv) != 4:  # Checking if correct number of args was passed.
        print(__doc__)
        sys.exit(1)

    user_name, password, database = sys.argv[1:]  # Extracting cmd_line args
    db = ms.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database,
            charset="utf8",
            port=3306)  # Connecting to specified database in terminal.

    cursor = db.cursor()  # Creating cursor to traverse the database.
    cursor.execute("SELECT * FROM states ORDER BY states.id")  # Getting states
    rows = cursor.fetchall()  # Listing all retrieved rows.
    for row in rows:  # Printing all the rows.
        print(row)

    db.close()  # Closing the connection to the database.
