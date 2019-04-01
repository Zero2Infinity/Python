from itertools import combinations

if __name__ == '__main__':
    _ = int(input())
    my_list = input().split()
    r = int(input())
    comb_list = list(combinations(my_list, r))
    a_exists = 0
    '''for comb in comb_list:
        if 'a' in comb:
            a_exists += 1 '''
    a_exists = filter(lambda c: 'a' in c, comb_list)
    #print (*a_exists)
    print ("{0:.3}".format(len(list(a_exists))/len(comb_list)))
