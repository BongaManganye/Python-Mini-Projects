# Leap Year Checker
# Write a function that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400

def is_leap_year(year):
    return(year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)
