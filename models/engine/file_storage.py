#!/usr/bin/python3
"""for defining FileStorage class"""

import os
import json
import uuid
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """
    Representing abstracted storage engine
    Attr:
    __file.path (name of the file to save objects to)
    __objects (instatiated objects in dictionarry form)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the __objects dictionary"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects with key <obj_class_name>.id"""
        objClassName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objClassName, obj.id)] = obj

    def save(self):
        """Serialization of __objects to the JSON __file_path"""
        fileDict = FileStorage.__objects
        objDict = {obj: fileDict[obj].to_dict() for obj in fileDict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objDict, f)

    def reload(self):
        """Deserialization of __file_path to __objects, if it exist"""
        try:
            with open(FileStorage.__file_path) as f:
                objDict = json.load(f)
                for i in objDict.values():
                    className = i["__class__"]
                    del i["__class__"]
                    self.new(eval(className)(**i))
        except FileNotFoundError:
            return "The file is missing"
