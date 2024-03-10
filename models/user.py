#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects
    Attribute:
    email: the email of the user
    password: password of the user
    first_name: first name of the user
    last_name: last name of the user

    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
