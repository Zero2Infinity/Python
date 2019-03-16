from itertools import combinations_with_replacement

if __name__ == '__main__':
    line = input().split()
    s, r = line[0], int(line[1])
    L = list(combinations_with_replacement(sorted(s), r))
    for l in L:
        print (''.join(l))


'''
Pythonian way:
print (*[''.join(p) for p in combs(sorted(word), int(r))] , sep='\n'])
'''
    
    
