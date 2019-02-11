from collections import deque

if __name__ == '__main__':
    d = deque()
    lines = []
    for _ in range(int(input())):
        lines.append('d.{0}({1})'.format(*input().split()+['']))
        ' unpackaged args list + empty char for pop() syntax to avoid out of index err'
        
    print (lines)

