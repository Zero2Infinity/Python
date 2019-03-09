def avg(arr):
    distinct_height = set(arr)
    return (sum(distinct_height)/len(distinct_height))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print (avg(arr))
