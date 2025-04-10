#!/usr/bin/env python3


def area_sum(rectangles):
    total = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        total = total + area

    return total
