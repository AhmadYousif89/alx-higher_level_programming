#!/usr/bin/python3
"""
Lists all City objects with their parent State
from the database hbtn_0e_101_usa
"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )

    with Session(engine) as session:
        data = session.query(City, State.name).join(State).all()
        for city, state_name in data:
            print(f"{city.id}: {city.name} -> {state_name}")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import State

    main()
