#!/usr/bin/env python3


def find_min(nums):
    minimum = float("inf")
    for number in nums:
        # Compare number with minimum
        if number < minimum:
            # What should you do if number is smaller than minimum?
            minimum = number
    return minimum
