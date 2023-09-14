#!/usr/bin/python3
"""Module to list all states starting with 'N'
    from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


def n_states():
    """Function to list all states starting with 'N'
        from the database hbtn_0e_0_usa takes argument
    """

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    n_states()
