#!/usr/bin/python3
"""square module for representing the square class."""


class square():
    """square class."""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Intializing the object with the given input"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Calculates the area of the square."""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Calculates the perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the sqare object."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
