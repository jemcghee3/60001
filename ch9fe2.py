# Introduction to Computation and Programming Using Python (2021)
# Chapter 9, Finger Exercise 2

"""Finger exercise: Implement a function that satisfies the
specification"""

def find_an_even(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even
    number"""
    for i in L:
        if i % 2 == 0:
            return i
    raise ValueError('L does not contain an even number.')

test_list = [i for i in range(1, 10, 2)]
test_test_2 = [i for i in range(10)]

print(find_an_even(test_list))
print(find_an_even(test_test_2))