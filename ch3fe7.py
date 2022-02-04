# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 7
"""
Add some code to the implementation of
Newton–Raphson that keeps track of the number of iterations used
to find the root. Use that code as part of a program that compares the
efficiency of Newton–Raphson and bisection search. (You should
discover that Newton–Raphson is far more efficient.)

Newton-Raphson for square root
Find x such that x**2 - 24 is within epsilon of 0
epsilon = 0.01
guess = k/2
while abs(guess**2 - k) >= epsilon:
    guess = guess - ((guess*22) - k)/(2*guess))
print('Square root of', k, 'is about', guess)
"""

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0

k = int(input("Enter a value for k: "))
epsilon = 0.01
guess = k/2
counter = 0
while abs(guess**2 - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    counter += 1
print('Square root of', k, 'is about', guess)
print("counter", counter)

low = 0
high = max(1, k)
bi_guess = (high + low) / 2
bi_counter = 1
while abs(bi_guess**2 - k) >= epsilon:
    print("low = ", low, "high = ", high, "bi_guess =", bi_guess)
    if bi_guess**2 < k:
        low = bi_guess
    else:
        high = bi_guess
    bi_guess = (high + low) / 2
    bi_counter += 1
print('Square root of', k, 'is about', bi_guess)
print("counter", bi_counter)
