#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()
    first_state = session.query(State).first()
    print(f"1: {first_state.name}" if first_state else "Nothing")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
