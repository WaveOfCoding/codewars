# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]


# My Solution
def maps(a):
    return [number * 2 for number in a]


# Another Solution
def maps(a):
    num = []
    for i in a:
        num.append(i * 2)
    return num