#!/usr/bin/python3
"""
connect to mysql database and query all the states
in the database passed as argument
"""
from sys import argv
import MySQLdb

db = MySQLdb.connect(host=argv[1], user=argv[2], passwd=argv[3], db=argv[4])
cur = db.cursor()
cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)
