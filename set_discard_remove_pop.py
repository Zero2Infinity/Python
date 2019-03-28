if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    s = set(nums)
    ops = int(input())
    for _ in range(ops):
        inp = input().split()
        getattr(s, inp[0])(*inp[1] if len(inp) > 1 else [])
        print (s)
    
