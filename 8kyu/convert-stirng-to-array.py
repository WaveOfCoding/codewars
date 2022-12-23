# Write a function to split a string and convert it into an array of words.
# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]


# My Solution
def string_to_array(s):
    return s.split(" ")


# Another Solution
def string_to_array(s):
    words = []
    if s == '':
        words.append(s)
    else:
        words = s.split()
    return words


