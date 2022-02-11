# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 4
"""
Write a function mult that accepts either one or
two ints as arguments. If called with two arguments, the function
prints the product of the two arguments. If called with one argument,
it prints that argument.
"""

def mult(int1, int2 = None):
    if int2 == None:
        print(int1)
    else:
        print(int1 * int2)

mult(5)
mult(5, 6)
