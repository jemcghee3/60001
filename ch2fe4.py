# Introduction to Computation and Programming Using Python (2021)
# Chapter 2, Finger Exercise 4
"""
Write a program that asks the user to input 10
integers, and then prints the largest odd number that was entered. If
no odd number was entered, it should print a message to that effect.
"""

counter = 0
numbers = []
while counter < 10:
    new_number = int(input(f"Please enter an integer. {10-counter} remaining. ")) # no input checking
    if new_number%2 != 0:
        numbers.append(new_number)
    counter += 1
print(max(numbers) if len(numbers) > 0 else "No odd number was entered.")
