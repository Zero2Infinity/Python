from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input().split())
marks = [int(Student._make(input().split()).MARKS) for _ in range(n)]
print ( '%.2f' % (sum(marks)/n) ) 
