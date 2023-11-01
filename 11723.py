import sys
input = sys.stdin.readline

N = int(input())
numbers = set()
for _ in range(N):
    command = list(map(str, input().split()))
    if len(command) == 1:
        if command[0] == 'all':
            numbers = set([i for i in range(1, 21)])
        else:
            numbers = set()
    else:
        func, x = command[0], command[1]
        x = int(x)
        if func == 'add':
            numbers.add(x)
        elif func == 'remove':
            numbers.discard(x)
        elif func == 'check':
            if x in numbers:
                print(1)
            else:
                print(0)
        elif func == 'toggle':
            if x in numbers:
                numbers.discard(x)
            else:
                numbers.add(x)
