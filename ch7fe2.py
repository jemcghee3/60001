# Introduction to Computation and Programming Using Python (2021)
# Chapter 7, Finger Exercise 2
"""Finger exercise: Since 1958, Canadian Thanksgiving has occurred
on the second Monday in October. Write a function that takes a year
(>1957) as a parameter, and returns the number of days between
Canadian Thanksgiving and Christmas.
"""

import calendar

def shopping_days(year):
    """year a number > 1957
    returns the number of days between Canadian Thanksgiving
    and Christmas in year"""
    # calculate the date of Canadian Thanksgiving each year
    turkey_day = find_canadian_thanksgiving(year) # do Canadians eat turkey for Thanksgiving?
    # calculate how many more days are after Thanksgiving in October
    oct_shopping_days = october_days_left(turkey_day)
    # add the 30 days in November
    nov_shopping_days = 30
    # add the 24 day in December before christmas
    dec_shopping_days = 24
    # return the sum
    return oct_shopping_days + nov_shopping_days + dec_shopping_days

def find_canadian_thanksgiving(year):
    """code given in book for November, modified for October
    year a number >= 1941
    returns the date in October for Canadian Thanksgiving that year"""
    month = calendar.monthcalendar(year, 10)
    if month[0][calendar.MONDAY] != 0:
        thanksgiving = month[1][calendar.MONDAY]
    else:
        thanksgiving = month[2][calendar.MONDAY]
    return thanksgiving

def find_canadian_thanksgiving_checker():
    for i in range(1958,2022):
        print(f'In {i}, Thanksgiving was on October {find_canadian_thanksgiving(i)}')

# find_canadian_thanksgiving_checker()

def october_days_left(d):
    """d is an integer representing the date in October for Canadian Thanksgiving
    returns the remaining days in October"""
    return 31 - d

def shopping_days_checker():
    for i in range(1958,2022):
        print(f'In {i}, there were {shopping_days(i)} shopping days between Canadian Thanksgiving and Christmas.')

shopping_days_checker()