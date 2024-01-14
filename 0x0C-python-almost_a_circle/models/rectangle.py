#!/usr/bin/python3

from models.base import Base

class Rectangle (Base):

    def __init__(self, width, height,  x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <=0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <=0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height))

    def display(self):
        print_symbol = "#"
        rectangle = ""

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += ("" * self.x) + (print_symbol * self.width) + '\n'
            print(rectangle, end="")


    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.height = args[1]
            self.width = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):

        return ({'x': getattr(self, "x"),
            'y': getattr(self, "y"), 'id': getattr(self, "id"),
            'height': getattr(self, "height"), 'width': getattr(self, "width")})


