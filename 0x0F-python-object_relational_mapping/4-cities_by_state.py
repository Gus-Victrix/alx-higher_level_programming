#!/usr/bin/python3

"""
Lists all cities from the database hbtn_0e_4_usa

Usage: ./4-cities_by_state.py <mysql username>  <user password>  <database name>
"""

if __name__ == "__main__":
    from sys import argv, exit
    import MySQLdb as ms

    if len(argv) != 4:
        print(__doc__)
        exit(1)

    conn = ms.connect(  # Creating database connection
        host="localhost", # Hostname
        user=argv[1],     # Username
        passwd=argv[2],   # Password
        db=argv[3],       # Database name
        port=3306)        # Port number

    cur = conn.cursor()  # Cursor object

    cur.execute(
    "SELECT c.id, c.name, s.name\
    FROM cities c JOIN states s\
    ON c.state_id = s.state_id\
    ORDER BY c.id ASC")  # Executing query

    rows = cur.fetchall()  # Fetching all rows

    for row in rows:  # Iterating through the rows
        print(row)    # Printing each row

    cur.close()       # Closing cursor
    conn.close()      # Closing connection
