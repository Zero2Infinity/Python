def is_leap_2(year):
    if year%4 == 0 and year%100 == 0 and year%400 == 0:
        return True
    elif year%4 == 0 and year%100 != 0 and year%400 != 0:
        return True
    else:
        return False 

def is_leap(year):
    return year%4 == 0 and (year%100==0) == (year%400==0)

year = int(input())
print (is_leap(year))
