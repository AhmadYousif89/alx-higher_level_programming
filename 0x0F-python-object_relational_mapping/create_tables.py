#!/usr/bin/python3
"""Start link class to table in database hbtn_0e_6_usa"""

import sys
from model_state import Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    USER = sys.argv[1]
    PASSWD = sys.argv[2]
    DB = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{USER}:{PASSWD}@localhost/{DB}', pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
