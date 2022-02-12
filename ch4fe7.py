# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 7
"""
Use find to implement a function satisfying the
specification
def find_last(s, sub):
    s and sub are non-empty strings
    Returns the index of the last occurrence of sub in s.
    Returns None if sub does not occur in s
"""

def find_last(s, sub):
    """s and sub are non-empty strings
        Returns the index of the last occurrence of sub in s.
        Returns None if sub does not occur in s"""
    if s.find(sub) == -1: # this is the return value for s.find if it's not there
        return None
    else:
        ans = s.find(sub) # found it, so save it
        ans2 = find_last(s[s.find(sub)+1:], sub) # search remaining string for the sub
        if ans2 != None: # if None, then it wasn't found, so the one already found is last
            ans += ans2 + 1 # move ans to next occurence, add 1 because 0 of the following string should be counted
        return ans

print(find_last('abcbc', 'bc'))

# looking at above, I thought of this implimentation that is cleaner and probably faster

def find_last_2(s, sub):
    if s.find(sub) == -1:
        return None
    else:
        return len(s) - 1 - s[::-1].find(sub) # len of string, subtract 1 to get index,
            #count backwards through string to find last/'first' occurence
            #once have that location, take it off the len of s to get the index

print(find_last_2('abcbc', 'bc'))
