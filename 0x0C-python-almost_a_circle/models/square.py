#!/usr/bin/python3
"""Module to define class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns string representation of square"""
        x = self.x
        y = self.y
        size = self.width
        return f"[Square] ({self.id}) {x}/{y} - {size}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to assign attributes to key and no key worded
        argument
        Parameter:
            *arg: pointer to non key word argument
            **kwargs: pointer to keyworded argument
        """
        if args:
            attribute = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attribute[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """method that returns dictionary representation of square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
