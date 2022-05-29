#!/usr/bin/python3
""" in this file, i will create a empty class for square"""


class Square():
    """Define a square"""
    def __init__(self, size=0):
        """
        Args:
            size (int): size of square
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self, size):
        """
        Args:
            size (int): size of square
        Return:
            area of square
        """
        return self.__size ** 2
