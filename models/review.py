#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

# Las lineas de abajo es lo que quiero reemplazar en vez de lo de arriba
# (quitar los michi y borrar lo de arriba menos el sheabang)

"""This is the review class"""
# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship


# class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
#    __tablename__ = 'reviews'

#    text = Column(String(1024), nullable=False)
#    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
#    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
