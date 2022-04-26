# Introduction to Computation and Programming Using Python (2021)
# Chapter 5, Finger Exercise 2
"Write a list comprehension that generates all non-primes between 2 and 100."

print([x for x in range(2, 100) if not any(x % y == 0 for y in range(2, x))])