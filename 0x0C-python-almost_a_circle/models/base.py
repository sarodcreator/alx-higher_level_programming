#!/usr/bin/python3
import json
"""Base class"""

class Base:
    """Function to create Parent class"""


    __nb_objects = 0
    def __init__(self, id=None):
        """Method to instantiate an object"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None or len(list_dictionaries) == 0:

            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
    
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + "json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                recent = cls(1, 1)

            else:
                recent = cls(1)

            recent.update(**dictionary)
            return (recent)
    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:

            with open(filename, "r") as jsonfile:
                dic_list = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in dic_list])

        except FileNotFoundError:
            return ([])
