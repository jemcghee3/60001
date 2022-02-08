# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 2
"""
Write a function is_in that accepts two strings as
arguments and returns True if either string occurs anywhere in the
other, and False otherwise. Hint: you might want to use the built-in
str operator in.
"""

def is_in(str1, str2):
    if str1 in str2:
        return True
    if str2 in str1:
        return True
    else:
        return False


x = "abcd5"
y = "abc4"

print(is_in(x, y))
