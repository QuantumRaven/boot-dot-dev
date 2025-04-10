#!/usr/bin/env python3

# Arithmetic solution
# def number_sum(n):
#     return n * (n + 1) // 2


# Expected solution
def number_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
