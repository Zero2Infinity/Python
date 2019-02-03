def list_operations(N):
    command_list = ['']*N
    for i in range(N):
        command_list[i] = input().split()

    list = []
    for command in command_list:
        if command[0] == 'insert':
            eval('list.insert({}, {})'.format(command[1], command[2]))
        elif command[0] == 'print':
            print (list)
        elif command[0] == 'remove':
            eval('list.remove({})'.format(command[1]))
        elif command[0] =='sort':
            eval('list.sort()')
        elif command[0] == 'pop':
            eval('list.pop()')
        elif command[0] == 'reverse':
            eval('list.reverse()')
        elif command[0] == 'append':
            eval('list.append({})'.format(command[1]))


if __name__ == '__main__':
    N = int(input())
    # list_operations(N)
    list = []
    for _ in range(N):
        line = input().split()
        cmd = line[0]
        args = line[1:]
        
        if cmd != 'print':
            eval('list.{}{}'.format(cmd, tuple(map(int,args))))
        else:
            print (list)

