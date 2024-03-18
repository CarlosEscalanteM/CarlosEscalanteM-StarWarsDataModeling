import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    ID = Column(Integer, primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    email = Column(String(50), unique=True)
    password = Column(String(50))

class Character(Base):
    __tablename__ = "character"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    race = Column(String(20), nullable=False)
    loyal_to = Column(String(20), nullable=False)
    height = Column(Integer)
    weight = Column(Integer)

class Planet(Base):
    __tablename__ = "planet"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    population = Column(Integer)

class Starship(Base):
    __tablename__ = "starship"
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20))
    loyal_to = Column(String(20), nullable=False)
   
class FavoriteCharacters(Base):
    __tablename__ = "favorite-characters"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey("character.id"))
    character_relationship = relationship(Character)

class FavoritePlanets(Base):
    __tablename__ = "favorite-planets"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_relationship = relationship(User)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet_relationship = relationship(Planet)

class FavoriteStarships(Base):
    __tablename__ = "favorite-starships"
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_relationship = relationship(User)
    starship_id = Column(Integer, ForeignKey("starship.id"))
    starship_relationship = relationship(Starship)

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
