from itertools import groupby

if __name__ == '__main__':
    s = input()
    for k, g in groupby(s):
        print ('({}, {})'.format(len(list(g)), k), end=' ')

