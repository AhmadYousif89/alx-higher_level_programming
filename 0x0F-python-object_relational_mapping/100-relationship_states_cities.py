#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    # Create all tables (states, cities)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        # Insert state California
        california = State(name="California")
        session.add(california)
        # Insert city San Francisco
        san_francisco = City(name="San Francisco")
        session.add(san_francisco)
        # Establish the relationship between California and San Francisco
        california.cities.append(san_francisco)
        # Save changes
        session.commit()


if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City

    main()
