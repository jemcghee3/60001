# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 4
"""
Finger exercise: What would have to be changed to make the code
in Figure 3-5 work for finding an approximation to the cube root of
both negative and positive numbers? Hint: think about changing low
to ensure that the answer lies within the region being searched.

Figure 3-5:
    epsilon = 0.01
    num_guesses, low = 0, 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**2 - x) >= epsilon:
        print('low =', low, 'high = ', high, 'ans = ', ans)
        num_guesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print('number of guesses =', num_guesses)
    print(ans, 'is close to square root of', x)
"""
x = -25
epsilon = 0.01
num_guesses, low = 0, min(0, x) # set low to be the minimum of 0, x
high = max(1, x) 
ans = (high + low) / 2 
while abs(ans**3 - x) >= epsilon: # from ans**2 to ans**3 due to cube root
    print('low =', low, 'high = ', high, 'ans = ', ans)
    num_guesses += 1
    if ans**3 < x: # 2 to 3
        low = ans
    else: 
        high = ans
    ans = (high + low) / 2 
print('number of guesses =', num_guesses)
print(ans, 'is close to cube root of', x)
