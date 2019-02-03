if __name__ == '__main__':
    'Designer Door Mat (H x W)'
    H, W = map(int, input().split()) 
    str = '.|.'
    
    for i in range((H-1)//2):
        print (('.|.'*(i*2+1)).center(W, '-'))

    print ('WELCOME'.center(W, '-'))

    for i in reversed(range((H-1)//2)):
        print (('.|.'*(i*2+1)).center(W, '-'))




