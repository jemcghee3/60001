# Introduction to Computation and Programming Using Python (2021)
# Chapter 7, Finger Exercise 3

"""Finger exercise: Write a program that first stores the first ten
numbers in the Fibonnaci sequence to a file named fib_file. Each
number should be on a separate line in the file. The program should
then read the numbers from the file and print them."""

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

with open('fib_file.txt', 'w') as fib_handle:
    for i in range(10):
        fib_handle.write(str(fib(i)) + '\n')

with open('fib_file.txt', 'r') as fib_handle:
    for line in fib_handle:
        print(line)