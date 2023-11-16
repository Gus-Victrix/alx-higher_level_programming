#!/usr/bin/python3

"""
List of the cities of the 4 argurment
"""

import MySQLdb
import sys

if "__main__" == __name__:
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states WHERE states.id =\
            cities.state_id AND states.name = %s",
        (sys.argv[4],),
    )
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
