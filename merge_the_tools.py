'''
def merge_the_tools_2 (string, k):
    ' simplest way to solve this problem '
    for i in range(0, len(string), k):
        slicedStr = string[i:i+k]
        unique = []
        for c in slicedStr:
            if c not in unique:
                unique.append(c)
        print (''.join(unique))    
'''

def merge_the_tools(string, k):
    ' k = 3; three copies of iterator(string); zip over it '
    itr = iter(string)
    for part in zip(*([itr]*3)):
        d = dict()
        print (([d.setdefault(c,c) for c in part if c not in d]))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
