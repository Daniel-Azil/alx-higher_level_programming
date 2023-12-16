#!/usr/bin/python3

""" A script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__=="__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                       passwd=sys.argv[2], db=sys.argv[3],
                                       port=3306)
    cursor = database_connect.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    records = cursor.fetchall()
    for values in records:
        print(values)
    cursor.close()
    database_connect.close()
