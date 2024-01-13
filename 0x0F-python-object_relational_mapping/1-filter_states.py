#!/usr/bin/python3

"""
Lists all states with a name starting with N from hbtn_0e_0_usa database.

Usage: ./1-filter_states.py <mysql username, mysql password, database name>
"""

if __name__ == "__main__":  # import guard
    import MySQLdb  # import MySQLdb module for MySQL connections
    import sys  # import sys module for command line arguments

    if len(sys.argv) != 4:  # check for valid number of arguments
        print(__doc__)  # print module documentation
        sys.exit(1)  # exit with error code 1 if conditions not met

    conn = MySQLdb.connect(  # connect to database
        host="localhost",  # host name
        port=3306,  # port number
        user=sys.argv[1],  # user supplied username
        passwd=sys.argv[2],  # user supplied password
        db=sys.argv[3],  # user supplied database name
        charset="utf8",  # set encoding
    )

    cur = conn.cursor()  # create cursor object
    # execute SQL query on cursor object
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()  # store query results in rows variable

    for row in rows:  # iterate through rows variable
        print(row)

    cur.close()  # close cursor
    conn.close()  # close connection to database
