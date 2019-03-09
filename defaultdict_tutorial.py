from collections import defaultdict
if __name__ == '__main__':
    group_A = defaultdict(list)
    group_B = []
    n, m = map(int, input().split())
    for i in range(1, n+1):
        group_A[input()].append(str(i))     # append as string value otherwise join wont work
    for j in range(m):
        group_B.append(input())

    for v in group_B:
        if len(group_A[v]) > 0:
            print (' '.join(group_A[v]))    # OR use map(str, [1, 2, 4]) so that join works
        else:
            print ('-1')
