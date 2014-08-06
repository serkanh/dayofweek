import math
import calendar


def convert_to_int(x):
    return int(x)

month_list = [calendar.month_name[i] for i in xrange(1,13)]

#create a dictionary for day to month
month_dict = dict(enumerate(month_list, start=1))


def dayoftheweek(date_input):
    #split format 02-16-1981
    month, ddate, year = date_input.split("-")
    century_digits = int(year[:2])
    year_digits = int(year[2:])
    month = int(month)
    year = int(year)
    ddate = int(ddate)
    value = year_digits + math.floor(year_digits/4)
    if century_digits == 18:
        value += 2
    elif century_digits == 20:
        value += 6
    else:
        value = value

    if month_dict[month] == 'January' and is_leapyear(year) == False:
        value += 1

    elif month_dict[month] == 'February' and is_leapyear(year) == True:
        value += 3

    elif month_dict[month] == 'February' and is_leapyear(year) == False:
        value += 4


    elif month_dict[month] == 'March' or month_dict[month] == 'November':
        value += 4

    elif month_dict[month] == 'May':
        value += 2

    elif month_dict[month] == 'June':
        value += 5

    elif month_dict[month] == 'August':
        value += 3

    elif month_dict[month] == 'October':
        value += 1

    elif month_dict[month] == 'September' or month_dict[month] == 'December':
        value += 6


    pre_result = value + ddate
    result = pre_result % 7


    if result == 1:
        print("Day of the week was Sunday")
    elif result == 2:
        print("Day of the week was Monday")
    elif result == 3:
        print("Day of the week was Tuesday")
    elif result == 4:
        print("Day of the week was Wednesday")
    elif result == 5:
        print("Day of the week was Thursday")
    elif result == 6:
        print("Day of the week was Friday")
    elif result == 0:
        print("Day of the week was Saturday")

#Determines if year is leap year or not
def is_leapyear(x):
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 == 0:
            return True
        else:
            return False
    else:
        return False


#http://www.millersville.edu/~bikenaga/number-theory/calendar/calendar.html
dayoftheweek("02-16-1981")
dayoftheweek("10-04-1982")

