from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    od = OrderedDict()
    for _ in range(n):
        # entry = input().split()
        # item, price = ' '.join(entry[:-1]), entry[-1]
        item, space, price = input().rpartition(' ')
        od[item] = od.get(item, 0) + int(price)

    for k, v in od.items():
        print (k, v)

