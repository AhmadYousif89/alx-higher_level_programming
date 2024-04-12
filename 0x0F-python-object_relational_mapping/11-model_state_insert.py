#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    NEW_STATE = "Louisiana"
    new_state = State(name=NEW_STATE)
    with Session.begin() as session:
        session.add(new_state)
        state = session.query(State).filter(State.name == NEW_STATE).first()
        print(f"{state.id}" if state else "Failed to insert!")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
