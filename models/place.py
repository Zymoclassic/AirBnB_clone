#!/usr/bin/python3
"""For defining the place class"""

from models.base_model import BaseModel
class Place(BaseModel):
    """
    Represents Place
    Attr:
    name (place name)
    city_id (the id of the city)
    user_id (the id of the user)
    description (description of the place)
    numRooms (the number of rooms)
    numBathroom (the number of bathrooms)
    guestMax (maximum number of guest that the place can contain)
    priceForANight (amount charged per night)
    latitude (the latitude of the place)
    longitude (the longitude of the place)
    amenity_id (list of amenity and their ids)
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    numRooms = 0
    numBathroom = 0
    guestMax = 0
    priceForANight = 0.0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []
