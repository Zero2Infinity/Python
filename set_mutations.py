if __name__ == '__main__':
    _ = int(input())
    setA = set(input().split())
    totalOperations = int(input())
    for _ in range(totalOperations):
        method, *_ = input().split()
        getattr(setA, method)(input().split())

    print (sum(map(int,setA)))

