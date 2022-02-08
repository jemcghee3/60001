# Introduction to Computation and Programming Using Python (2021)
# Chapter 4, Finger Exercise 3

# Write a function to test is_in

def is_in(str1, str2):
    if str1 in str2:
        return True
    if str2 in str1:
        return True
    else:
        return False

def test_is_in(strings):
    for s in strings:
        for t in strings:
            result = is_in(s, t)
            print(f"str1 = {s}, str2 = {t}: {result}")

strings = ("abc", "abcd", "1bc", "a2c", "abcde")
test_is_in(strings)
