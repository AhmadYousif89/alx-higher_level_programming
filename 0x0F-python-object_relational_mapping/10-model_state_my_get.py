#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
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
    target = sys.argv[4]
    state = session.query(State).filter(State.name == target).first()
    print(f"{state.id}" if state else "Not found")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
