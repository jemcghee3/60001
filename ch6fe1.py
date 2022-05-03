# Introduction to Compuation and Computer Programming Using Python (2021)
# Chapter 6, Finger Exercise 1
"""Finger exercise: The harmonic sum of an integer, n > 0, can be
calculated using the formula 1 + 1/2 + ... + 1/n. Write a recursive function
that computes this."""

def find_harm_sum(i):
    """i: an integer > 0
    takes an integer and returns the harmonic sum"""
    if i == 1:
        # print("base case: return 1")
        return 1
    harm_sum = 1/i + find_harm_sum(i-1)
    # print("non-base case: return ", harm_sum)
    return harm_sum

test_i = int(input("Input an integer greater than 0: "))
find_harm_sum(test_i)