#!/usr/bin/env python3


def fizzbuzz(start, end):
    output = []
    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            output.append("fizzbuzz")
        elif num % 3 == 0:
            output.append("fizz")
        elif num % 5 == 0:
            output.append("buzz")
        else:
            output.append(num)
    return output
