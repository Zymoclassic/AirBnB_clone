#!/usr/bin/python3
"""For defining the city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    Represents City.
    Attr :
        name (city's name).
        state_id (the state id).
    """

    name = ""
    state_id = ""
