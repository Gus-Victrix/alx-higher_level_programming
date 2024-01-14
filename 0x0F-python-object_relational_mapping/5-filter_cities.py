#!/usr/bin/python3

"""
Lists all cities from the state in database hbtn_0e_4_usa

Usage: ./4-cities_by_state.py <mysql username> <user password> <database name>
        <state name searched>
"""

if __name__ == "__main__":
    from sys import argv, exit
    import MySQLdb as ms

    if len(argv) != 5:
        print(__doc__)
        exit(1)
    conn = ms.connect(     # Creating database connection
        host="localhost",  # Hostname
        user=argv[1],      # Username
        passwd=argv[2],    # Password
        db=argv[3],        # Database name
        port=3306)         # Port number
    cur = conn.cursor()    # Cursor object
    cur.execute(
        "SELECT c.name\
         FROM cities c JOIN states s\
         ON c.state_id = s.id\
         WHERE s.name = %s\
         ORDER BY c.id ASC", (argv[4],))  # Executing query
    rows = cur.fetchall()  # Fetching all rows
    print(', '.join(row[0] for row in rows))  # Printing combined rows
    cur.close()       # Closing cursor
    conn.close()      # Closing connection
