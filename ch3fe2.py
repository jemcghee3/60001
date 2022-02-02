# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 2
"""
Finger exercise: Write a program that asks the user to enter an
integer and prints two integers, root and pwr, such that 1 < pwr < 6
and root**pwr is equal to the integer entered by the user. If no such
pair of integers exists, it should print a message to that effect.
"""

user_num = int(input("Please enter an integer: "))
root = None
pwr = None
breaker = 0
for r in range(2, user_num):
    if breaker != 0:
        break
    for p in range(1, 6):
        if r**p > user_num:
            break # no need to check higher powers
        elif r**p == user_num:
            root = r
            pwr = p
            breaker = 1 # breaks once a match is found
            print("Match found.")
            print("root", root)
            print("pwr", pwr)
            print("root**pwr", root**pwr)
            break # match found, no need to keep going
if root == None: # no match was found
    print(f"There is no such pair of integers pwr and root such that 1 < pwr < 6 and root**pwr is equal to {user_num}.")
