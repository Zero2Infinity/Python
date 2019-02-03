if __name__ == '__main__':
    'HackerRank logo using text alignment'
    thickness = int(input()) # odd number
    c = 'H' 

    for i in range(thickness):
        print ((c*((i*2)+1)).center(2*thickness))

    for i in range(thickness+1):
        print ('{}{}'.format(((c*thickness).center(2*thickness)), \
                            ((c*thickness).center(6*thickness))))
        
    for i in range((thickness+1)//2):
        print ('{}'.format((c*thickness*5).center(6*thickness)))

    for i in range(thickness+1):
        print ('{}{}'.format(((c*thickness).center(2*thickness)), \
                            ((c*thickness).center(6*thickness))))
        
    for i in reversed(range(thickness)):
        print ('{}{}'.format((''.rjust(thickness*4)), (c*(i*2+1)).center(2*thickness)))

