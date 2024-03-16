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
    user = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
