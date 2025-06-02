import sys

n = int(sys.stdin.readline().rstrip())

collect = set()
lst = [str(i) for i in range(1, 21)]

for i in range(n):
    string = sys.stdin.readline().rstrip()
    command, element = '', ''
    if string == 'all' or string == 'empty':
        command = string
    else:
        command, element = string.split(' ')

    if command == 'add':
        collect.add(element)
    elif command == 'check':
        if element in collect:
            print(1)
        else:
            print(0)
    elif command == 'remove':
        collect.discard(element)
    elif command == 'toggle':
        if element in collect:
            collect.discard(element)
        else:
            collect.add(element)
    elif command == 'all':
        collect = set(lst)
    else:
        collect.clear()