def is_leap_year(year):
    if year / 4 == 0 and year / 400 != 0:
        return True
    elif year / 100 == 0 and year / 400 == 0:
        return True
    else:
        return False


def getMonthDays(year, month):
    days = 31
    if month == 2:
        if is_leap_year(year):
            days = 29
        else:
            days = 28
    elif month in [4,6,9,11]:
        days = 30
    return days

def getTotalDays(year, month):
    totalDays = 0
    for i in range(1990, year):
        if is_leap_year(i):
            totalDays += 366
        else:
            totalDays += 365

    for i in range(1, month):
        totalDays += getMonthDays(year, i)

    return totalDays
