# Create the function fridayTheThirteenths that accepts a start year and an end year (inclusive),
# and returns all of the dates where the 13th of a month lands on a Friday in the given range of year(s).

# The return value should be a string where each date is seperated by a space. The date should be formatted
# like 9/13/2014 where months do not have leading zeroes and are separated with forward slashes.
# If no end year is given, only return friday the thirteenths during the start year.

# fridayTheThirteenths(1999, 2000)
# // returns
# "8/13/1999 10/13/2000"

# fridayTheThirteenths(2014, 2015)
# // returns
# "6/13/2014 2/13/2015 3/13/2015 11/13/2015"

# fridayTheThirteenths(2000)
# // returns
# "10/13/2000"


from datetime import date, timedelta
def friday_the_thirteenths(start, end=None):
    dates = []
    step = timedelta(days=1)
    start_year = date(start, 1, 1)
    if end:
        end_year = date(end, 12, 31)
        while start_year < end_year:
            if start_year.weekday() == 4 and start_year.day == 13:
                res = '/'.join(map(str, [start_year.month, 13, start_year.year]))
                dates.append(res)
            start_year += step
    else:
        while start_year < date(start, 12, 31):
            if start_year.weekday() == 4 and start_year.day == 13:
                res = '/'.join(map(str, [start_year.month, 13, start_year.year]))
                dates.append(res)
            start_year += step
    return ' '.join(dates)