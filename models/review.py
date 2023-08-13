#!/usr/bin/python3
"""for defining the Review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Representing review
    Attr:
    place_id (the place id)
    user_id (the user id)
    text (the content of the review)
    """

    place_id = ""
    user_id = ""
    text = ""
