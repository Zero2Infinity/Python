if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a//b)
        except (ZeroDivisionError, ValueError) as e:  # OR could use Exception higher exception class
            print('Error Code: {}'.format(e))
            
