if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))

    print (setA, setB)
    happiness = 0
    for n in nums:
       if n in setA:
            happiness += 1
       if n in setB:
            happiness -= 1

    print (happiness)  
    
