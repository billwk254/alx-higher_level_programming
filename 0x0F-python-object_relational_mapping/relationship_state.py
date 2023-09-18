#!/usr/bin/python3


"""
Contains the class definition of a State.
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State class that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
