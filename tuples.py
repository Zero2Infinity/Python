if __name__ == '__main__':
    n = int(input())
    int_list = map(int, input().split())
    print (hash(tuple(int_list)))
