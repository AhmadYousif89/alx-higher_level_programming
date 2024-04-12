#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""


def main():
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Session = sessionmaker(engine)
    target_id = 2
    new_state_name = "New Mexico"
    with Session.begin() as session:
        session.query(State).filter(State.id == target_id).update(
            {State.name: new_state_name}
        )


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    main()
