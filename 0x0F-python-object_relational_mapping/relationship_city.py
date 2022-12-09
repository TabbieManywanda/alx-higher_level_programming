#!/usr/bin/python3
'''relationship with State'''

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    '''relationship with class State'''
    __tablename__ = 'cities'
    id = Column(
            Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer, ForeignKey('states.id'),
            nullable=False)
    state = relationship('State', back_populates='cities')
