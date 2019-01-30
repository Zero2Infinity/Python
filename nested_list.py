if __name__ == '__main__':
    students = []
    N = int(input())
    for _ in range(N):
        name  = input()
        score = float(input())
        students.append([name, score])

    # Ordered based on score in descending order
    # rev_students = sorted(students, key=lambda student: student[1], reverse=True)

    '''
    To avoid looping over again to find second lowest score; I should have though of using Set type
    to take out duplicate values and I can be confident that second from the end is second lowest value.
    # find second lowest score
    for s in reversed(rev_students): 
        if s[1] != rev_students[-1][1]:
            second_lowest = s[1]
            break
    '''

    second_lowest = sorted(list(set([marks for names, marks in students])))[1]

    '''
    # compare with second last score and store all names and print in alphabetic order
    names = [s[0] for s in rev_students if ( second_lowest == s[1])]
    names.sort()

    # I don't know how to print list with new line in-between
    for n in names:
        print(n)
    '''

    print ('\n'.join([a for a,b in sorted(students) if b == second_lowest]))

