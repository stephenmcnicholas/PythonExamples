def is_year_leap(year):

    if(year%4==0 and year%100!=0):
        return True
    elif(year%400==0):
        return True
    else:
        return False


def days_in_month(year, month):
    mon = [31,28,31,30,31,30,31,31,30,31,30,31]
    if(is_leap_year(year) and month==2):
        return 29
    else:
        return mon[month-1]
    

def day_of_year(year, month, day):
    
    mon = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(month-1):
        days += mon[i]
    days += day
    if(is_year_leap(year)):
        days += 1
    return days
    
print(day_of_year(1900, 12, 31))
