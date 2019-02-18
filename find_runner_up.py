import sys
import collections
def find_second_max_num(arr):
    ' This is python way '
    o = collections.OrderedDict.fromkeys(sorted(arr),0)
    o.popitem()                 # Pop last times (highest number)
    print (o.popitem()[0])      # popitem returns tuple (0, 1)

def find_second_max_num_2(arr):
    ' This is old school (c++) way '
    first_max = -sys.maxsize - 1
    second_max = -sys.maxsize - 1
    for n in arr[:]:
        if n > first_max:
            second_max = first_max
            first_max = n
        elif n > second_max and n < first_max:
            second_max = n
   
    print (second_max) 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    find_second_max_num_2(arr)
