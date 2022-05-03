# Introduction to Computation and Programming Using Python (2021)
# Chapter 7, Finger Exercise 1
"""Finger exercise: Write a function that meets the specification
"""

import calendar

def shopping_days(year):
    """year a number >= 1941
    returns the number of days between U.S. Thanksgiving
    and Christmas in year"""
    # calculate the date of Thanksgiving each year
    turkey_day = find_thanksgiving(year)
    # calculate how many more days are after Thanksgiving in November
    nov_shopping_days = november_days_left(turkey_day)
    # add the 24 day in December before christmas
    dec_shopping_days = 24
    # return the sum
    return nov_shopping_days + dec_shopping_days

def find_thanksgiving(year):
    """code given in book
    year a number >= 1941
    returns the date in November for Thanksgiving that year"""
    month = calendar.monthcalendar(year, 11)
    if month[0][calendar.THURSDAY] != 0:
        thanksgiving = month[3][calendar.THURSDAY]
    else:
        thanksgiving = month[4][calendar.THURSDAY]
    return thanksgiving

def find_thanksgiving_checker():
    for i in range(1941,2022):
        print(f'In {i}, Thanksgiving was on November {find_thanksgiving(i)}')

# find_thanksgiving_checker()

def november_days_left(d):
    """d is an integer representing the date in November for Thanksgiving
    returns the remaining days in November"""
    return 30 - d

def shopping_days_checker():
    for i in range(1941,2022):
        print(f'In {i}, there were {shopping_days(i)} shopping days between Thanksgiving and Christmas.')

shopping_days_checker()