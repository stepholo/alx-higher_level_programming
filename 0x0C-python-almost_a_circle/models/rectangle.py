#!/usr/bin/python3
"""Module to define class rectangle"""


from models.base import Base


class Rectangle(Base):
    """class rectangle to define attributes of a rectangle
       it inherits from parent class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Arg:
           value: the value for the width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Arg:
           value: the value for the height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        Arg:
           value: the value assigned to x
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter
        Arg:
          value: the value assigned to y
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def to_csv_row(self):
        """method that gets an instance attribute values into a list"""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def create_from_csv_row(cls, row):
        """method that creates from csv list"""
        id, width, height, x, y = map(int, row)
        return cls(id, width, height, x, y)

    def area(self):
        """method that returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """method that prints represantation of the rectangle using #"""
        x = self.__x
        w = self.__width
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            if i < self.__height - 1:
                print("{}{}".format(' ' * x, '#' * w))
            else:
                print("{}{}".format(' ' * x, '#' * w), end='\n')

    def __str__(self):
        """method that returns string representation of the rectangle"""
        x = self.__x
        y = self.__y
        h = self.__height
        w = self.__width
        return f"[Rectangle] ({self.id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """method that assigns an argument to each attribute
        args:
            *args: Pointer to the list of non-keyword argument
            **kwargs: Pointer to the key-worded argument
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that returns dictionaty representation of the class"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
