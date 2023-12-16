#!/usr/bin/python3

""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3],
                               port=3306)
    cursor = database_connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    records = cursor.fetchall()
    for values in records:
        print(values)
    cursor.close()
    database_connect.close()
