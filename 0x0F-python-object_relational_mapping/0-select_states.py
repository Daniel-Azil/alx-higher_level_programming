#!/usr/bin/python3

""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    dataBase_connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                       passwd=sys.argv[2], db=sys.argv[3],
                                       port=3306)
    cursor = dataBase_connect.cursor()
    cursor.execute("SELECT * FROM states")
    records = cursor.fetchall()
    for values in records:
        print(values)
    cursor.close()
    dataBase_connect.close()
