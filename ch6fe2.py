# Introduction to Computation and Computer Programming Using Python (2021)
# Chapter 6, Finger Exercise 2
"""Finger exercise: When the implementation of fib in Figure 6-3 is
used to compute fib(5), how many times does it compute the value
of fib(2) on the way to computing fib(5)?"""

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    global fib_2_counter
    if n == 2:
        fib_2_counter += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_fib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
    print('fib(2) computed', fib_2_counter, 'times.')

fib_2_counter = 0
test_fib(5)