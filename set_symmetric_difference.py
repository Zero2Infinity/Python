if __name__ == '__main__':
    n = int(input())
    setA = set(map(int, input().split()))
    m = int(input())
    setB = set(map(int, input().split()))
    
    print (len(setA ^ setB))


'''
_, a, _, b = eval( set(input().split()), "*4); print(len(a|b)

'''
