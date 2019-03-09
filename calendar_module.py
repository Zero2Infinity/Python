import calendar

if __name__ == '__main__':
    date = list(map(int, input().split()))
    day_of_week = (calendar.weekday(date[2], date[0], date[1]))
    print (calendar.day_name[day_of_week].upper())

