import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(32), nullable=False)
    username: Mapped[str] = mapped_column(String(32))
    favoritos: Mapped["Favorites"] = relationship(back_populates="user")

class People(Base):
    __tablename__ = 'people'
    id: Mapped[str] = mapped_column(primary_key=True)
    birth_year: Mapped[str] = mapped_column(String(32))
    eye_color: Mapped[str] = mapped_column(String(32))
    films: Mapped["Films"] = relationship(back_populates="people")
    gender: Mapped[str] = mapped_column(String(32))
    hair_color: Mapped[str] = mapped_column(String(32))
    height: Mapped[str] = mapped_column(String(8))
    homeworld: Mapped["Planets"] = relationship(back_populates="people")
    mass: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    species: Mapped["Species"] = relationship(back_populates="people")
    starships: Mapped["Starships"] = relationship(back_populates="people")
    vehicles: Mapped["Vehicles"] = relationship(back_populates="people")
    favoritos: Mapped["Favorites"] = relationship(back_populates="people")
    
class Films(Base):
    __tablename__ = 'films'
    id: Mapped[str] = mapped_column(primary_key=True)
    characters: Mapped["People"] = relationship(back_populates="films")
    director: Mapped[str] = mapped_column(String(32))
    episode_id: Mapped[str] = mapped_column(String(1))
    opening_crawl: Mapped[str] = mapped_column(String(32))
    planets: Mapped["Planets"] = relationship(back_populates="films")
    producer: Mapped[str] = mapped_column(String(32))
    release_date: Mapped[str] = mapped_column(String(32))
    species: Mapped["Species"] = relationship(back_populates="films")
    starships: Mapped["Starships"] = relationship(back_populates="films")
    title: Mapped[str] = mapped_column(String(32))
    vehicles: Mapped["Vehicles"] = relationship(back_populates="films")

class Starships(Base):
    __tablename__ = 'starships'
    id: Mapped[str] = mapped_column(primary_key=True)
    mglt: Mapped[str] = mapped_column(String(16))
    cargo_capacity: Mapped[str] = mapped_column(String(16))
    consumables: Mapped[str] = mapped_column(String(16))
    cost_in_credits: Mapped[str] = mapped_column(String(32))
    crew: Mapped[str] = mapped_column(String(16))
    hyperdrive_rating: Mapped[str] = mapped_column(String(4))
    length: Mapped[str] = mapped_column(String(16))
    manufacturer: Mapped[str] = mapped_column(String(32))
    max_atmosphering_speed: Mapped[str] = mapped_column(String(8), nullable=True)
    model: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(32))
    passengers: Mapped[str] = mapped_column(String(8))
    films: Mapped["Films"] = relationship(back_populates="starships")
    pilots: Mapped["People"] = relationship(back_populates="starships")
    startship_class: Mapped[str] = mapped_column(String(32))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id: Mapped[str] = mapped_column(primary_key=True)
    cargo_capacity: Mapped[str] = mapped_column(String(16))
    consumables: Mapped[str] = mapped_column(String(16))
    cost_in_credits: Mapped[str] = mapped_column(String(32))
    crew: Mapped[str] = mapped_column(String(16))
    length: Mapped[str] = mapped_column(String(16))
    manufacturer: Mapped[str] = mapped_column(String(32))
    max_atmosphering_speed: Mapped[str] = mapped_column(String(8), nullable=True)
    model: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(32))
    passengers: Mapped[str] = mapped_column(String(8))
    pilots: Mapped["People"] = relationship(back_populates="vehicles")
    films: Mapped["Films"] = relationship(back_populates="starships")
    vehicle_class: Mapped[str] = mapped_column(String(32))

class Species(Base):
    __tablename__ = 'species'
    id: Mapped[str] = mapped_column(primary_key=True)
    average_height: Mapped[str] = mapped_column(String(8))
    average_lifespan: Mapped[str] = mapped_column(String(8))
    classification: Mapped[str] = mapped_column(String(16))
    designation: Mapped[str] = mapped_column(String(16))
    eye_colors: Mapped[str] = mapped_column(String(128))
    hair_colors: Mapped[str] = mapped_column(String(128))
    homeworld: Mapped["Planets"] = relationship(back_populates="species")
    language: Mapped[str] = mapped_column(String(32))
    name: Mapped[str] = mapped_column(String(32))
    people: Mapped["People"] = relationship(back_populates="species")
    films: Mapped["Films"] = relationship(back_populates="species")
    skin_colors: Mapped[str] = mapped_column(String(32))

class Planets(Base):
    __tablename__ = 'planets'
    id: Mapped[str] = mapped_column(primary_key=True)
    climate: Mapped[str] = mapped_column(String(32))
    diameter: Mapped[str] = mapped_column(String(16))
    films: Mapped["Films"] = relationship(back_populates="planets")
    gravity: Mapped[str] = mapped_column(String(8))
    name: Mapped[str] = mapped_column(String(32))
    orbital_period: Mapped[str] = mapped_column(String(8))
    population: Mapped[str] = mapped_column(String(16))
    residents: Mapped["People"] = relationship(back_populates="planets")
    rotation_period: Mapped[str] = mapped_column(String(8))
    surface_water: Mapped[str] = mapped_column(String(3))
    terrain: Mapped[str] = mapped_column(String(32))
    favoritos: Mapped["Favorites"] = relationship(back_populates="planets")

class Favorites(Base):
    __tablename__ = 'favorites'
    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey('user.id'), nullable=False)
    people_id: Mapped[str] = mapped_column(ForeignKey('people.id'))
    films_id: Mapped[str] = mapped_column(ForeignKey('films.id'))
    starships_id: Mapped[str] = mapped_column(ForeignKey('starships.id'))
    vehicles_id: Mapped[str] = mapped_column(ForeignKey('vehicles.id'))
    species_id: Mapped[str] = mapped_column(ForeignKey('species.id'))
    planets_id: Mapped[str] = mapped_column(ForeignKey('planets.id'))
    
    user: Mapped["User"] = relationship(back_populates="favorites")
    people: Mapped["People"] = relationship(back_populates="favorites")
    films: Mapped["Films"] = relationship(back_populates="favorites")
    starships: Mapped["Starships"] = relationship(back_populates="favorites")
    vehicles: Mapped["Vehicles"] = relationship(back_populates="favorites")
    species: Mapped["Species"] = relationship(back_populates="favorites")
    planets: Mapped["Planets"] = relationship(back_populates="favorites")

# Genera el diagrama ER
render_er(Base, 'diagram.png')