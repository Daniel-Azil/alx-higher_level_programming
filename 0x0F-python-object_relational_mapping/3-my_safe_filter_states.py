#!/usr/bin/python3

""" A a script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa where name matches
    the argument. It is a script that is safe from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    database_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                       passwd=sys.argv[2], db=sys.argv[3],
                                       port=3306)

    cursor = database_connect.cursor()
    cursor.execute("""SELECT * FROM states WHERE name=%s ORDER BY id ASC""",
                   (sys.argv[4],))
    records = cursor.fetchall()

    for values in records:
        print(values)

    cursor.close()
    database_connect.close()
