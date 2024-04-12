#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter (a)
from the database hbtn_0e_6_usa
"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    with Session.begin() as session:
        states = session.query(State).where(State.name.contains('a')).all()
        for state in states:
            session.delete(state)


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
