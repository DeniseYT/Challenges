# Given a string with a month and a year (separated by a space), return the number of days in that month.
# Leap years are a bit tricky. A year is a leap year if and only if:
# it is evenly divisible by 4
# except if it is divisible by 100, in which case it isn’t
# except if it is divisible by 400, in which case it is
# So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 2000 is divisible by 400, so it was.


# Start my solution:

def is_leap_year(year):

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

def days_in_month(date):

    month, year = date.split()
    month = int(month)
    year = int(year)

    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    
    if month in {1,3,5,7,8,10,12}:
        return 31
    
    if month in {4,6,9,11}:
        return 30

print(days_in_month("03 2015"))