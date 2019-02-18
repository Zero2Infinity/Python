def possible_to_stack_2(cubes):
    index_1 = 0
    index_2 = len(cubes)
    for i in range(0, len(cubes)-1):
        index_1 = i
        if cubes[i] < cubes[i+1]:
            break
            
    for j in range(len(cubes)-1, 0, -1):
        index_2 = j
        # Don't like that I needed two conditions
        if (cubes[j] < cubes[j-1]) or (index_2 <= index_1):
            break

    # two pointers are not meeting due to loops
    if index_2 - index_1 <= 1:
        return "Yes"
    else:
        return "No" 

def possible_to_stack(cubes):
    i = 0
    l = len(cubes)
    while i < l-1 and cubes[i] >= cubes[i+1]:
        i += 1
    while i < l-1 and cubes[i] <= cubes[i+1]:
        i += 1

    return "Yes" if i == l-1 else "No"

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        cubes = tuple(map(int, input().split()))
        print(possible_to_stack(cubes))
