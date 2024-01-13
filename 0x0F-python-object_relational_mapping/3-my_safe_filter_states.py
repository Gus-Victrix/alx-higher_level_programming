#!/usr/bin/python3

"""
Display all values in states table of hbtn_0e_0_usa where name matches argv[4].
This time it's safe from SQL injections!

Usage: ./0-select_states.py <username> <password> <database name> <state name>
"""

if __name__ == "__main__":  # Execute only if run as script
    import sys  # Exit error and commandline arguemnts access
    import MySQLdb  # Connecting to mysql database.

    if len(sys.argv) != 5:  # Check if the user input is valid
        print(__doc__)  # Print the documentation
        sys.exit(1)  # Exit with error

    argv = sys.argv  # Assigning sys.argv to argv for easier access
    if not argv[4].isalpha():  # Protecting against SQL injections
        print("Argument 4 must be a string")
        sys.exit(1)
    conn = MySQLdb.connect(  # Connecting to MySQL database
                username=argv[1],  # The database username.
                passwd=argv[2],  # User password.
                host="localhost",  # Location of the db
                charset="utf8",  # Character set used in the database.
                port=3306,  # Port to be used for connections
                db=argv[3])  # Database to be used for connection.
    cur = conn.cursor()  # Creating cursor object
    # Execute the query to the database
    cur.execute("SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()  # Fetch all the rows in a list
    for row in rows:  # Loop through all rows
        if row[1] == argv[4]:  # Check if the row matches the state name
            print(row)  # Print each row

    cur.close()  # Close all cursors
    conn.close()  # Close all databases
