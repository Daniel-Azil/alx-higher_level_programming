#!/usr/bin/python3

""" A script that lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                       passwd=sys.argv[2], db=sys.argv[3],
                                       port=3306)

    cursor = database_connect.cursor()
    cursor.execute(""""SELECT cities.id, cities.name, states.name
                   FROM states INNER JOIN cities
                   ON states.id = cities.state_id
                   ORDER BY cities.id ASC""")
    cursor.fetchall()
    records = cursor.fetchall()

    for values in records:
        print(values)

    cursor.close()
    database_connect.close()
