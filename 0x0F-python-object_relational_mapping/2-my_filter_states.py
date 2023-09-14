#!/usr/bin/python3
"""Module that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument.
"""


import MySQLdb
from sys import argv


def format_states():
    """Function that takes in an argument and displays
        all values in the states table of hbtn_0e_0_usa
        where name matches the argument.
    """

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    name = argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )

    cur = db.cursor()
    querry = "SELECT * FROM states WHERE name LIKE '{}%';".format(name)
    cur.execute(querry)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    format_states()
