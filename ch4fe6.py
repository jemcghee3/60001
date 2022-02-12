# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 6
"""
Finger exercise: Write a lambda expression that has two numeric
parameters. If the second argument equals zero, it should return
None. Otherwise it should return the value of dividing the first
argument by the second argument. Hint: use a conditional
expression.
"""
divider = lambda x, y: None if y == 0 else x / y
print(divider(4, 2))
print(divider(4, 0))

