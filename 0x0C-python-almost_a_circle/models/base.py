#!/usr/bin/python3

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

