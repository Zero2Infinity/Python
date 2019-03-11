if __name__ == '__main__':
    m, M = int(input()), map(int, input().split())
    n, N = int(input()), map(int, input().split())

    setM = set(M)
    setN = set(N)

    setO = set()
    setO.update(setM.difference(setN))
    setO.update(setN.difference(setM))
    
    print ('\n'.join(map(str,sorted(setO))))


'''
Two liner
a,b [set(input().split()) for _ in range(4)][1::2]
print (*sorted(a^b, key=int), sep = '\n')
'''
