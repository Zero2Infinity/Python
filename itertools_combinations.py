from itertools import combinations

if __name__ == '__main__':
    inp = input().split()
    for i in range(1, int(inp[1])+1):
        for j in list(combinations(sorted(inp[0]), i)):
            print (''.join(j))
