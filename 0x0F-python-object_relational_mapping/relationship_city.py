#!/usr/bin/python3
"""Defines the City class for the database table (cities)"""

from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """Represents the cities table in the database hbtn_0e_14_usa"""

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
