#!/usr/bin/env python3

def divide_list(nums, divisor):
    output = []
    for num in nums:
        new_value = num / divisor
        output.append(new_value)
    return output
