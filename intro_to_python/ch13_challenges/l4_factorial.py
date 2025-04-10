#!/usr/bin/env python3

# Correct answer 1
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         fact = 1
#         for i in range(1, num + 1):
#             fact = fact * i
#         return fact


# Correct answer 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
