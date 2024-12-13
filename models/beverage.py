"""Beverage module"""

# Landon Lamie
# 12/11/2024

# Third party imports
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import (
    String,
    Float,
    Boolean
)

# Base class for other models to inherit from
Base = declarative_base()


class Beverage(Base):
    """Class to represent a single beverage"""

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