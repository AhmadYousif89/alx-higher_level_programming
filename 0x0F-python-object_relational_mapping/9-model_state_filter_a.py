#!/usr/bin/python3
"""
Lists all State objects that contain the letter (a)
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
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
