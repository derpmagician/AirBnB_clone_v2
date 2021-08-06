#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

# Las lineas de abajo es lo que quiero reemplazar en vez de lo de arriba
# (quitar los michi y borrar lo de arriba menos el sheabang)

"""This module defines a class User"""
# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship

# class User(BaseModel, Base):
#     """This is the class for user
#     Attributes:
#         email: email address
#         password: password for you login
#         first_name: first name
#         last_name: last name
#     """

#     __tablename__ = 'users'

#     email = Column(String(128), nullable=False)
#     password = Column(String(128), nullable=False)
#     first_name = Column(String(128))
#     last_name = Column(String(128))
#     places = relationship('Place', backref='user')
#     reviews = relationship('Review', backref='user')