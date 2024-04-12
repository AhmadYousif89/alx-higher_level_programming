#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    session = Session()
    data = session.query(State, City).join(State).all()
    for state, city in data:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    from model_city import City

    main()
