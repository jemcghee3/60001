# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 6
"""
Finger exercise: The Empire State Building is 102 stories high. A
man wanted to know the highest floor from which he could drop an
egg without the egg breaking. He proposed to drop an egg from the
top floor. If it broke, he would go down a floor, and try it again. He
would do this until the egg did not break. At worst, this method
requires 102 eggs. Implement a method that at worst uses seven
eggs.
"""

egg = 1 # number of broken eggs
low = 1 # first floor
high = 102 # top floor
limit = 28 # arbitrary floor for breakage
test_floor = 0

while test_floor != limit:
    crack = None # did the egg break?
    test_floor = int((high+low)/2)
    print(f"Test Floor {test_floor}; Egg {egg}")
    egg += 1
    if test_floor > limit:
        crack = True
    if crack == True: # egg broke
        high = test_floor
    else: # egg did not break
        low = test_floor

