# Introduction to Computation and Programming Using Python (2021)
# Chapter 2, Finger Exercise 1
# Finger exercise: Write a program that examines three variables—
# x, y, and z—and prints the largest odd number among them. If none
# of them are odd, it should print the smallest value of the three.

x = 10 # largest, not odd
y = 5 # largest odd
z = 1 # smallest odd


numbers = [x, y, z]
numbers.sort()
biggestOdd = None # so anything is bigger
smallest = None # so anything is smaller
for n in numbers:
    if n%2 == 1 and (biggestOdd == None or n > biggestOdd): #both biggest and odd
        biggestOdd = n
    if smallest == None or n < smallest: # the first number is the smallest, then it compares
        smallest = n

if biggestOdd != None:
    print("The largest odd number is", biggestOdd)
else:
    print("There is no odd number. The smallest number is", smallest)

