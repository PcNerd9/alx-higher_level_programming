#!/usr/bin/python3

"""
query the database for all the states that start with N using
MySQLdb module
"""
from sys import argv
import MySQLdb

db = MySQLdb.connect(host=argv[1], user=argv[2], passwd=argv[3], db=argv[4])
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
states = cur.fetchall()
for state in states:
    print(state)
