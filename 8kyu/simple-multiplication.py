# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# My Solution
def simple_multiplication(number):
    num = int()
    if number % 2 == 0:
        num = number * 8
    else:
        num = number * 9
    return num


# Another Solution
def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9
