#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

# Las lineas de abajo es lo que quiero reemplazar en vez de lo de arriba
# (quitar los michi y borrar lo de arriba menos el sheabang)

""" City Module for HBNB project """
# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.orm import relationship


# class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

#    __tablename__ = 'cities'

#    name = Column(String(128), nullable=False)
#    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
#    places = relationship('Place', backref='cities')
