#!/usr/bin/python3
'''Python file similar to model_state.py'''

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''contains the class definition of a City'''
    __tablename__ = 'cities'
    id = Column(
            Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer, ForeignKey('states.id'),
            nullable=False)
