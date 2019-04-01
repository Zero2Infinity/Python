if __name__ == '__main__':
    n = int(input())

    # Palindromic triangle
    s = [] 
    for i in range(1,n+1):
        s.append(str(i))
        print ( ''.join(s[:-1] + s[::-1]) )
