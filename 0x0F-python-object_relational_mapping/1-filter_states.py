#!/usr/bin/python3

"""
query the database for all the states that start with N using
MySQLdb module
"""
from sys import argv
import MySQLdb


def main():
    """
    the entry to the main program
    """
    host = argv[1]
    user = argv[2]
    password = argv[3]
    database = argv[4]
    db = MySQLdb.connect(host=host, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
