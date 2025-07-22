#!/usr/bin/env python3

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        left_most = min(self.__x1, self.__x2)
        return left_most

    def get_right_x(self):
        right_most = max(self.__x1, self.__x2)
        return right_most

    def get_top_y(self):
        top_most = max(self.__y1, self.__y2)
        return top_most

    def get_bottom_y(self):
        bottom_most = min (self.__y1, self.__y2)
        return bottom_most

    # don't touch below this line

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

