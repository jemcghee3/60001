# Introduction to Computation and Programming Using Python (2021)
# Chapter 2, Finger Exercise 5

"""
Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to use a for loop that is a primality test nested inside a for loop that
iterates over the odd integers between 3 and 999.
"""

"""
This is my answer that does not take the hint above.
Find all non-primes because the range is small.
Everything else is prime.

answer = 0 #set initial answer
non_prime = [2]
for f in range(2, 501):
    non_prime.append(2*f)
for i in range(3, 500, 2):
    if i in non_prime:
        continue
    for f in range (i, 1000//i+1):
        non_prime.append(f*i)
#        print(f"Appending {f*i} as non-prime.")
non_prime.sort()
for i in range (3, 1001):
    if i not in non_prime:
#        print(f"Prime found: {i}")
        answer += i
print(f"The sum of primes greater than 2 and less than 1000 is {answer}.")
"""

answer = 0
for i in range(3, 1000, 2):
    for number in range(2, i+1): # i comes from higher loop, i+1 so number == i at the end (no factors found)
        if number == i:
            # then number is prime
#            print(f"Prime found! {number}")
            answer += number
        elif i%number == 0: # then i is not prime
#            print(f"{i} % {number} is {i%number}.")
            break
print(f"The sum of primes greater than 2 and less than 1000 is {answer}.")
