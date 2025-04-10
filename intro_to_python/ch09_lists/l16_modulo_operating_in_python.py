#!/usr/bin/env python3


def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        odd_nums = i % 2
        if odd_nums:
            odd_numbers.append(i)

    return odd_numbers
