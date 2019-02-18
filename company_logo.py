import string
def most_common_characters_in_order(s):
    d = dict.fromkeys(string.ascii_lowercase, 0)     # This is a savior - set right order
    for c in s:
        d[c] = d.get(c, 0) + 1

    print (d)
    sorted_x = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    print (sorted_x)
    [print (*item) for item in sorted_x[:3]]

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    s = input()
    d = most_common_characters_in_order(s)
    '''
    print(OrderedCounter(sorted(s)))
    [print (*c) for c in OrderedCounter(sorted(s)).most_common(3)]    
    '''
# Alternate way: sort key and value and print first three from each
