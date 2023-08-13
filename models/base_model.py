#!/usr/bin/python3

"""Defines the class BaseModel"""
import models
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """This is a representation of the HBnB project BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        for initializing a new BaseModel.
        Args:
        *args : any
        **kwargs : key/value pairs
        """

        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        for updating updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance
        Includes the key/value pair __class__ representing the class name of the object
        """
        savedict = self.__dict__.copy()
        savedict["created_at"] = self.created_at.isoformat()
        savedict["updated_at"] = self.updated_at.isoformat()
        savedict["__class__"] = self.__class__.__name__
        return savedict
    
    def __str__(self):
        """
        Return the string representation of the BaseModel instances
        """
        clientName = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(clientName, self.id, self.__dict__)
