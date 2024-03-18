#!/usr/bin/python3

"""
safely query a database
"""


def main():
    """
    the main program to run only as main
    """
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    arugment = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password, database=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY id", (arugment, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
