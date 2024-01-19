#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel

storage_type = getenv("HBNB_TYPE_STORAGE")

class Amenity(BaseModel, Base):
    """ documment doc """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity',
                                       back_populates="amenities")
    else:
        name = ""
