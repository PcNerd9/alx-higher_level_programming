#!/usr/bin/python3

"""
contain a function that query a database
"""


def main():
    import MySQLdb
    import sys
    """
    the main funcion of the program
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=user, password=password, database=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM State ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
