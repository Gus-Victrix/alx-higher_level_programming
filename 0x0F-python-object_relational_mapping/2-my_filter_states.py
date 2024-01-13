#!/usr/bin/python3

"""
Display all values in states table of hbtn_0e_0_usa where name matches argv[4].

Usage: ./0-select_states.py <username> <password> <database name> <state name>
"""

if __name__ == "__main__":  # Execute only if run as script
    import sys  # Exit error and commandline arguemnts access
    import MySQLdb  # Connecting to mysql database.

    if len(sys.argv) != 5:  # Check if the user input is valid
        print(__doc__)  # Print the documentation
        sys.exit(1)  # Exit with error

    conn = MySQLdb.connect(  # Connecting to MySQL database
                host="localhost",  # Location of the db
                port=3306,  # Port to be used for connections
                user=sys.argv[1],  # The database username.
                passwd=sys.argv[2],  # User password.
                db=sys.argv[3],  # Database to be used for connection.
                charset="utf8")  # Character set used in the database.
    cur = conn.cursor()  # Creating cursor object
    cur.execute(
        f"SELECT * FROM states WHERE name = '{sys.argv[4]}'\
        ORDER BY id ASC")  # Execute the query to the database
    rows = cur.fetchall()  # Fetch all the data returned by the query
    for row in rows:  # Loop through all rows
        if row[1] == sys.argv[4]:  # Check if the row matches the state name
            print(row)  # Print each row

    cur.close()  # Close all cursors
    conn.close()  # Close all databases
