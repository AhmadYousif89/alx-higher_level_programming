#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects
contained in the database hbtn_0e_101_usa
"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )

    with Session(engine) as session:
        states = session.query(State).all()
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import State

    main()
