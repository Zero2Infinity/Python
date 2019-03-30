if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = set(nums)
    ops = int(input())
    for _ in range(ops):
        inp, *args = input().split()
        getattr(s, inp)(*map(int, args))
        print (sum(s))
    
