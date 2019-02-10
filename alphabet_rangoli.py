import string
def rangoli(size):
    width = size * 4 - 3 
    start = 97
    pattern = []
    lines = []
    # First challenge to generate alphabets
    temp = []
    temp_lines = []

    for i in range(size):      # per line
        for j in range(i+1):          # per chars
            temp.append(chr(start+(size-j-1)))

        alphabets = temp[:]
        temp.pop()
        while len(temp):            # pop old values
            alphabets.append(temp.pop())

        temp_lines.append('-'.join(alphabets).center(width, '-'))

    # pop previous line by line
    lines = temp_lines[:]
    temp_lines.pop()
    while len(temp_lines):
        lines.append(temp_lines.pop())

    # print lines using join()
    print ('\n'.join(lines))
    
def rangoli_2(size):
    ' string slice and ascii_lowercase to match int index '
    width = size*4-3
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        lines.append('-'.join((alpha[size-1:(size-1)-i:-1]) + (alpha[(size-1)-i:size:1])).center(width, '-'))

    print ('\n'.join(lines[:size-1] + lines[size-1::-1]))


def rangoli_3(size):
    ' finding indexes on alpha is bit complex; simplify it'
    width = size*4-3
    alpha = string.ascii_lowercase[:size]
    
    lines = []
    for i in range(size):
        #lines.append('-'.join(alpha[size-1:i:-1] + alpha[i:size+1]).center(width, '-'))
        lines.append('-'.join(alpha[-1:-2-i:-1] + alpha[size-i:size:1]).center(width, '-'))
    print ('\n'.join(lines[:size-1] + lines[size-1::-1]))
    
if __name__ == '__main__':
    size = int(input())
    rangoli_3(size)
