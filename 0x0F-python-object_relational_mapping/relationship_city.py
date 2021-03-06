#!/usr/bin/python3
""" module of class city that inherits from base """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from relationship_state import Base, State

Base = declarative_base()


class City(Base):
    ''' class State that inherits from Base '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
