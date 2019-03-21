from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    oc = OrderedCounter(words)
    print(len(oc))
    #print (' '.join([str(v) for k,v in oc.items()]))
    print (*oc.values())

