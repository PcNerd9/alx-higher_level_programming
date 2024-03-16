#!/usr/bin/python3
"""
connect to mysql database and query all the states
in the database passed as argument
"""


def main():
    """
    the entry to the main program
    """
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306,  user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
