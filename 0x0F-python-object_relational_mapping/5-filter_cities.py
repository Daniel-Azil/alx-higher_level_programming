#!/usr/bin/python3

"""
    A script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    database_connect = MySQLdb(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               port=3306)

    cursor = database_connect.cursor()
    cursor.execute("""SELECT cities.name
                   FROM states INNER JOIN cities
                   ON states.id = cities.state_id
                   WHERE states.name LIKE %s
                   ORDER BY cities.id ASC""", (sys.argv[4],))

    records = cursor.fetchall()

    for values in records:
        print(values)

    cursor.close()
    database_connect.close()
