from datetime import datetime as dt

if __name__ == '__main__':
    n = int (input() )
    for _ in range(n):
        str_date1, str_date2 = input(), input() 
        date1 = dt.strptime(str_date1, "%a %d %b %Y %H:%M:%S %z")
        date2 = dt.strptime(str_date2, "%a %d %b %Y %H:%M:%S %z")
        diff = abs(date1 - date2)
        print ( int(diff.total_seconds()) )
