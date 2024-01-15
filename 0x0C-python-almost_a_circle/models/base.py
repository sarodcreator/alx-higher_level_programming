#!/usr/bin/python3
"""Base module"""

import json
import csv
import turtle



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
         """A function that returns JSON representation of a list of dicts"""

        if list_dictionaries is None or len(list_dictionaries) == 0:

            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
    
    @classmethod
    def save_to_file(cls, list_objs):
        """A function that Writes JSON serialization of objects to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """A function that returns the deserialization of a JSON string"""

        if json_string is None or json_string == "[]":
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """A function that returns a class instantied from a dictionary"""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                recent = cls(1, 1)

            else:
                recent = cls(1)

            recent.update(**dictionary)
            return (recent)
    @classmethod
    def load_from_file(cls):
        """A function that returns a list of classes instantiated from JSON"""

        filename = str(cls.__name__) + ".json"
        try:

            with open(filename, "r") as jsonfile:
                dic_list = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in dic_list])

        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A function that writes the CSV serialization of objects to a file"""
        
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                else:
                    fieldnames = ["id", "size", "x", "y"]

                write_file = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    write_file.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a CSV file and returns a list of instances."""

        filename = cls.__name__ + ".csv"
        try:

            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]

                else:
                    fieldnames = ["id", "size", "x", "y"]

                dict_list = csv.DictReader(csvfile, fieldnames=fieldnames)
                dict_list = [dict([k, int(v)] for k, v in d.items())
                              for d in dict_list]
                return ([cls.create(**d) for d in dict_list])

        except FileNotFoundError:
            return ([])
          

    def draw(list_rectangles, list_squares):
        """A function that draws Rectangles & Squares using turtle module."""

        mod = turtle.Turtle()
        mod.screen.bgcolor("#000000")
        mod.pensize(3)
        mod.shape("turtle")

        mod.color("black")
        for items in list_rectangles:
            mod.showturtle()
            mod.up()
            mod.goto(items.x, items.y)
            mod.down()

            for i in range(2):
                mod.forward(items.width)
                mod.left(90)
                mod.forward(items.height)
                mod.left(90)
            mod.hideturtle()

        mod.color("green")
        for square in list_squares:
           mod.showturtle()
            mod.up()
            mod.goto(square.x, square.y)
            mod.down()

            for i in range(2):
                mod.forward(square.width)
                mod.left(90)
                mod.forward(sq.height)
                mod.left(90)
            mode.hideturtle()

        turtle.exitonclick()
