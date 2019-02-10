import string
def solve(s):
    words = s.split(' ')
    result = []
    for w in words:
        result.append(w.capitalize()) 

    return ' '.join(result)

if __name__ == '__main__':
    s = input()
    # print(solve(s))
    print (string.capwords(s, ' '))
