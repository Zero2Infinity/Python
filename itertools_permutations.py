from itertools import permutations

if __name__ == '__main__':
    inp = input().split()
    string = inp[0]
    length = int(inp[1])
    for i in permutations(sorted(string), length):
        print (''.join(i))

