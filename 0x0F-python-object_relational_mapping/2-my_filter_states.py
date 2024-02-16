#!/usr/bin/python3
"""
query the database for all the states in the
State table with a particular name
"""

import MySQLdb
import sys

def main():
    """
    the main function that queries the database
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    argument = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, password=password, database=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM State WHERE name=%s ORDER BY id", (argument,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()
