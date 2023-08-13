#!/usr/bin/python3
"""for defining the user class"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Representing User
    Attr:
    firstName (User's first name)
    lastName (User's last name)
    emailAddress (User's email address)
    password (User's password)
    """

    firstName = ""
    lastName = ""
    emailAddress = ""
    password = ""
