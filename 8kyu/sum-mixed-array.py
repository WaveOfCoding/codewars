# Given an array of integers as strings and numbers,
# return the sum of the array values as if all were numbers.

# Return your answer as a number.

# My Solution
def sum_mix(arr):
    return sum([int(x) for x in arr])


# Another Solution
def sum_mix(arr):
    return sum(map(int, arr))