#!/usr/bin/python3

"""
query the database to list all the cities from the database
hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    the main program
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN \
            states WHERE cities.state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
