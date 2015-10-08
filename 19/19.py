"""
   You are given the following information, but you may prefer to do some
   research for yourself.

     • 1 Jan 1900 was a Monday.
     • Thirty days has September,
       April, June and November.
       All the rest have thirty-one,
       Saving February alone,
       Which has twenty-eight, rain or shine.
       And on leap years, twenty-nine.
     • A leap year occurs on any year evenly divisible by 4, but not on a
       century unless it is divisible by 400.

   How many Sundays fell on the first of the month during the twentieth
   century (1 Jan 1901 to 31 Dec 2000)?
"""

def is_leapyear(n):
    """Returns true if n is a leap year"""
    return not n % 4 and (n % 100 != 0 or not n % 400)

def days_in_month(n, leapyear=False):
    """Returns the number of days in the nth month of the year"""
    if n in (4, 6, 9, 11):
        return 30
    if n == 2:
        return 29 if leapyear else 28
    return 31

if __name__ == '__main__':
    year_start, weekday, year_end = 1901, 1, 1999

    sundays = 0
    for year in range(year_start, year_end + 1):
        for month in range(1, 12 + 1):
            days = days_in_month(month, leapyear=is_leapyear(year))
            for day in range(1, days + 1):
                if weekday == 7:
                    if day == 1:
                        sundays += 1
                    weekday = 0
                weekday += 1

    print(sundays)


"""
NOTE:
The solution above only works for ranges that start from the first day 
of a year to the last day of another. This is sufficient for the given 
problem. Accomodating to start or end from a specific day of the year can 
be done trivially by changing the for loops into while loops.

Days in a month are numbered 1 through 28/29/30/31 (depending on the month).
Months in a year are numbered 1 (Jan) through 12 (Dec).
Weekdays are numbered 1 (Monday) through 7 (Sunday).
"""
