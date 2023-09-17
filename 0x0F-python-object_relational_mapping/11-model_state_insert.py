#!/usr/bin/python3
"""Sript that lists all State objects
    from the database hbtn_06_usa
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def list_first_state():
    """Function to add another state
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    louisiana = State(name="Louisiana")

    session.add(louisiana)

    session.commit()

    print(f'{louisiana.id}')


if __name__ == '__main__':
    list_first_state()
