#!/usr/bin/python3
"""Module that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


def using_join():
    """Function that takes in the name of a state as an argument
        and lists all cities of that state, using the database hbtn_0e_4_usa
    """

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

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
            "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id;"
            )

    cur.execute(querry, (state_name,))
    result = cur.fetchone()
    if result and result[0]:
        print(result[0])


if __name__ == '__main__':
    using_join()
