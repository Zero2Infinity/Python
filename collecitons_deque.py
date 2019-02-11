from collections import deque

if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        eval('d.{0}({1})'.format(*input().split()+['']))
    ' unpackaged args list + empty char for pop() syntax to avoid out of index err'
        
    print (*d)

'''
idea: getattr is build class.append(1) or class.pop()
for _ in range(int(input())):
    in = input().split()
    getattr(d, in[0])(*in[1] i len(in) > 1 else [])

print (*[it for it in d])
'''
