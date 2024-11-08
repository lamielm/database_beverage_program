"""Beverage data models"""

# System Imports.
import os

# First-Party imports
from program import session
from user_interface import UserInterface

# Third-Party imports
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Float, Boolean

# Base class for other models to inherit from
Base = declarative_base()

ui = UserInterface

class Beverage(Base):
    """Beverage class"""

    __tablename__ = "beverages"

    id = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    pack = Column(String(255), nullable=False)
    price = Column(Float(2), nullable=False)
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


class BeverageCollection:
    """BeverageCollection class"""

    def __init__(self):
        """Constructor"""
        self.__beverages = []

    def __str__(self):
        """String method"""
        return_string = ""
        for beverage in self.__beverages:
            return_string += f"{beverage}{os.linesep}"
        return return_string
    

    def add(self, id_, name, pack, price, active):
        """Add a new beverage to the collection"""
        new_beverage = Beverage(id_, name, pack, price, active)
        session.add(new_beverage)
        session.commit()

    def find_by_id(self, id_):
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
            
    # I have to edit add(Should be good?), change find to filter(might be good?  Haven't tested it), update, and delete CRUD
