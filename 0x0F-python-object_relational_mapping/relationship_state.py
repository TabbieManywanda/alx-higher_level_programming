#!/usr/bin/python3
'''relationship with city'''

from sqlalchemy import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''relationship with city class created'''
    __tablename__ = 'states'
    id = Column(
            Integer, autoincrement=True, nullable=False,
            unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')
