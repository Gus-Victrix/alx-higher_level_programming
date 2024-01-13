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
    conn = MySQLdb.connect(  # Connecting to MySQL database
                username=argv[1],  # The database username.
                passwd=argv[2],  # User password.
                host="localhost",  # Location of the db
                charset="utf8",  # Character set used in the database.
                port=3306,  # Port to be used for connections
                db=argv[3])  # Database to be used for connection.
    cur = conn.cursor()  # Creating cursor object
    # Execute the query to the database
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
            ORDER BY id ASC", (argv[4],))  # Defended from SQL injections
    rows = cur.fetchall()  # Fetch all the rows in a list
    for row in rows:  # Loop through all rows
        print(row)  # Print each row

    cur.close()  # Close all cursors
    conn.close()  # Close all databases
