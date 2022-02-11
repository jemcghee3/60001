# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 5
"""
 Using the algorithm of Figure 3-6, write a
function that satisfies the specification
def log(x, base, epsilon):
    Assumes x and epsilon int or float, base an int,
        x > 1, epsilon > 0 & power >= 1
    Returns float y such that base**y is within epsilon
of x.

Figure 3-6:
    # Find lower bound on ans
    lower_bound = 0
    while 2**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (high + low)/2
    while abs(2**ans - x) >= epsilon:
        if 2**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) /2
    print(ans, 'is close to the log base 2 of', x)
"""

def log(x, base, epsilon):
    """Assumes x and epsilon int or float, base an int,
        x > 1, epsilon > 0 & power >= 1
        Returns float y such that base**y is within epsilon
        of x.
    """

    # Find lower bound on ans
    lower_bound = 0
    while base**lower_bound < x:
        lower_bound += 1
    low = lower_bound - 1
    high = lower_bound + 1
    # Perform bisection search
    ans = (high + low)/2
    while abs(base**ans - x) >= epsilon:
        if base**ans < x:
            low = ans
        else:
            high = ans
        ans = (high + low) /2
    print(ans, 'is close to the log base', base, 'of', x)

log(10, 3, 0.0001)
