# Introduction to Computation and Programming Using Python (2021)
# Chapter 3, Finger Exercise 4
"""
Finger exercise: What would the code in Figure 3-5 do if x = -25?

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
num_guesses, low = 0, 0
high = max(1, x) # here it would set the high = 1
ans = (high + low) / 2 # now ans = 0.5
while abs(ans**2 - x) >= epsilon: # 25.25 is > epsilon on entry to loop
    print('low =', low, 'high = ', high, 'ans = ', ans)
    num_guesses += 1
    if ans**2 < x: # 0.25 is > -25, so this does not fire
        low = ans
    else: 
        high = ans # high = 0.25
    ans = (high + low) / 2 # ans = 0.125
    # this will run forever as ans approaches 0
    if ans < epsilon: # added for proof of understanding
        break # added for proof of understanding
print('number of guesses =', num_guesses)
print(ans, 'is close to square root of', x)
