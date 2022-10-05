#!/usr/bin/python3
"""Defining a class Square that
inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inheriting from
    Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a Square instance
        to be similar to Rectangle"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string defining Square properties"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if len(args) != 0:
            for count in range(len(args)):
                if count == 0 :
                    self.id = args[count]
                elif count == 1:
                    self.size = args[count]
                elif count == 2:
                    self.x = args[count]
                elif count == 3:
                    self.y = args[count]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
