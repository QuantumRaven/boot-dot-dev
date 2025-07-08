#!/usr/bin/env python3

class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        perm = 2 * (self.length + self.width)
        return perm


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

