#!/usr/bin/python3

"""
safely querys a database to list all the cities
of a state using the hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    """
    the main programm
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    argument = sys.argv[4]
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             password=password, database=database)
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities JOIN states WHERE\
            states.id = cities.state_id AND states.name = %s\
            ORDER BY cities.id", (argument,))
        states = cur.fetchall()
        if (len(states) > 0):
            for i in range(len(states) - 1):
                print(states[i][0], end=", ")

            print(states[len(states) - 1][0])
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
