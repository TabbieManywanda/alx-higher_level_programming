#!/usr/bin/python3
"""class Rectangle having a class attributed added
to specify symbol to be used when printing out an
instance
"""


class Rectangle:
    """class Rectangle definition"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing class Rectangle:
        Arguments - weight and height"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter method"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """printing out a rectanglewith '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(str(self.print_symbol) *
                         self.__width for x in range(self.__height))

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
