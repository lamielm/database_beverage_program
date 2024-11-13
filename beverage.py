"""Beverage data models"""

# System Imports.
import os

# Third-Party imports
from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import (String, Float, Boolean)


engine = create_engine("sqlite:///db.sqlite3", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Base class for other models to inherit from
Base = declarative_base()


class Beverage(Base):
    """Beverage class"""

    __tablename__ = "beverages"

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    pack = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    active = Column(Boolean, nullable=False)

    def __init__(self, id_, name, pack, price, active):
        """Constructor"""
        self.id = id_
        self.name = name
        self.pack = pack
        self.price = price
        self.active = active

    def __str__(self):
        """String method"""
        active = "True" if self.active else "False"
        return f"| {self.id:>6} | {self.name:<56} | {self.pack:<15} | {self.price:>6.2f} | {active:<6} |"


class BeverageRepository:
    """BeverageRepository class"""

    def __str__(self):
        """String method"""
        return_string = ""
        for beverage in session.query(Beverage).all():
            return_string += f"{beverage}{os.linesep}"
        return return_string


    
    def create_database(self):
        """Create the database tables based on the defined models"""
        Base.metadata.create_all(engine)

    def bulk_add(self, beverages):
        """Take in beverages list and commit it to DB"""
        for id_, name, pack, price, active in beverages:
            beverage = Beverage(
                id_ = id_,
                name = name,
                pack = pack,
                price = price,
                active = active
            )

            session.add(beverage)
        session.commit()

    def add(self, id_, name, pack, price, active): # Create
        """Add a new beverage to the collection"""
        new_beverage = Beverage(id_, name, pack, price, active)
        session.add(new_beverage)
        session.commit()

    def find_by_id(self, id_): #Read?
        """Find a beverage by it's id"""
        single_beverage_id = (
            session.query(
                Beverage, 
            )
            .filter(
                Beverage.id == id_
            )
            .first()
        )
        return single_beverage_id
        
    def update_existing(self, id_, name, pack, price, active):
        """Update an existing beverage"""
        beverage_to_update = (
                session.query(
                    Beverage,
                )
                .filter(
                    Beverage.id == id_,
                )
                .first()
            )
        
        beverage_to_update.name = name
        beverage_to_update.pack = pack
        beverage_to_update.price = price
        beverage_to_update.active = bool(active)
        session.commit()
    
    def delete_existing(self, id_):    
        """Delete an existing beverage"""         
        beverage_to_delete = (
            session.query(Beverage)
            .filter(
                Beverage.id == id_,
            )
            .first()
        )
        session.delete(beverage_to_delete)
        session.commit()
            