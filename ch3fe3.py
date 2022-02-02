# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 3
"""
Finger exercise: Write a program that prints the sum of the prime
numbers greater than 2 and less than 1000. Hint: you probably want
to have a loop that is a primality test nested inside a loop that
iterates over the odd integers between 3 and 999.
"""

# This was the same exercise as in Chapter 2, except it was hinted to use a for loop

answer = 0
for i in range(3, 1000, 2):
    for r in range(2, int(i/3)+2): # can't be 2, since it would be even, and the highest factor could be i/3
        # i/3+1 would include i/3, so have to add 2 to get one past that and ensure no factors found
        if r == int(i/3)+1:
            # then number is prime
#            print(f"Prime number found! {i}")
            answer += i
            break
        if i%r == 0:
            # not prime
#            print(f"{i} % {r} is {i%r}.")
            break
print(f"The sum of primes greater than 2 and less than 1000 is {answer}.")
