#!/usr/bin/python3

"""
query the database to select all the rows in the state
table
"""


def main():
    import MySQLdb
    import sys
    """
    the main function for the program
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, password=password, database=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM State ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        if (row[1].startswith("N")):
            print(row)


if __name__ == "__main__":
    main()
