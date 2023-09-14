#!/usr/bin/python3
"""Module that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def using_join():
    """Function to list all cities from the database hbtn_0e_4_usa
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
            )

    cur = db.cursor()
    querry = (
            "SELECT cities.id, cities.name AS city_name, states.name "
            "AS state_name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id;"
            )

    cur.execute(querry,)
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    using_join()
