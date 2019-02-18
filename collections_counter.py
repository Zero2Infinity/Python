from collections import Counter

if __name__ == '__main__':
    num_shoes = int(input())
    shoes = Counter(map(int, input().split()))
    num_cust = int(input())
    total_price = 0
    for _ in range(num_cust):
        size, price = map(int, input().split())
        if shoes[size] > 0:
            total_price += price
            shoes[size] -= 1

    print (total_price)

        
