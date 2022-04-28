# Introduction to Computation and Programming Using Python (2021)
# Chapter 5, Finger Exercise 4
"""Implement a function that meets the specification"""

def get_min(d):
    """d a dict mapping letters to ints
    returns the value in d with the key that occurs first in the
    alphabet. E.g., if d = {x = 11, b = 12}, get_min returns 12"""
    key_list = [k for k in d]
    key_list.sort()
    return d[key_list[0]]

d_test = {'x' : 11, 'b' : 12}

print(get_min(d_test))

# Note this does not deal with uppercase characters.