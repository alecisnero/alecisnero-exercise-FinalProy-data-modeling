import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(10), nullable=False)
    email = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    favorite_id  = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(String(250), nullable=True)
    vehicles_id = Column(String(250), nullable=True)
    planets_id = Column(String(250), nullable=True)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    character_id = Column(Integer, ForeignKey('favorite.character_id'), nullable=False)
    name = Column(String(250), nullable=False)
    description= Column(String(250), nullable=True)
    height= Column(Integer, nullable=True)
    age= Column(Integer, nullable=True)
    weight= Column(Integer, nullable=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, nullable=False)
    planets_id = Column(Integer, ForeignKey('favorite.planets_id'), nullable=False)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    rotation = Column(Integer, nullable=True)
    gravedad = Column(Integer, nullable=True)
    climate = Column(Integer, nullable=True)
    terreno = Column(Integer, nullable=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(String(250), primary_key=True, nullable=False) 
    vehicles_id = Column(String(250), ForeignKey('favorite.id'), nullable=False)
    name = Column(String(250), nullable=True)
    description = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
