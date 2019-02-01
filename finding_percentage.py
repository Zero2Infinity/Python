if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n): 
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # for loop is expensive..
    # print ('%.2f' % [(s[0]+s[1]+s[2])/3.0 for n, s in student_marks.items() if query_name == n][0])

    # Other ways to simplify this like
    query_score = student_marks[query_name]
    print ('%.2f' % (sum(query_score)/len(query_score)))
