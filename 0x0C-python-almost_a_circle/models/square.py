#!/usr/bin/python3

from models.rectangle import Rectangle

class Square (Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

        def __str__(self):

            return ("[{}] ({})  {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width))

    def to_dictionary(self):

        return ({'id': getattr(self, "id"), 'x': getattr(self, "x"),
                'size': getattr(self, "size"), 'y': getattr(self, "y")})

