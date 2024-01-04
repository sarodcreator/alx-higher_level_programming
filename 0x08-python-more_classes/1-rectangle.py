#!/usr/bin/python3
"""1. Definition of a Rectangle"""

class Rectangle:
    """Rectangle defines a rectangle"""
    width = 0
    height = 0
    def __init__(self, height, width):
        """Function that initializes instances for height and width"""
    
        self.width = width
        self.height = height

    @property
    def width(self):
         """Function that retrieves width instance attribute"""
         return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Function that retrieves height instance attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """
        function that sets height instance attribute
        Raise TypeError and ValueError if not integer or natural number resp.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
