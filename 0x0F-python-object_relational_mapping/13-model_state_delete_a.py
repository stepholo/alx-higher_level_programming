#!/usr/bin/python3
"""Sript that lists all State objects
    from the database hbtn_06_usa
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def delete_states_with_a_in_name():
    """Function to delete all state objects with letter 'a'
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).filter(
            ~State.name.like('%[^a]%')).all()

    if state:
        for st in state:
            session.delete(st)
        session.commit()


if __name__ == '__main__':
    delete_states_with_a_in_name()
