#!/usr/bin/python3
""" in this file, i will create a empty class for square"""


class Square():
    """Define a square"""

    def __init__(self, size=0):
        """Magic mehtod for initializating with size
        Args:

            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Property to retrieve the size.

        Property setter to set that check:
            * Size must be an integer, otherwise raise a TypeError
            * If size is less than 0, raise a ValueError
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method for calculated the area for square.

        Args:
            size (int): size of square
        Return:
            area of square
        """
        return self.__size ** 2
