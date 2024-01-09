from collections import deque

n = int(input())
l = deque([])
for _ in range(n):
    command = list(map(str, input().split()))
    if len(command) == 1:
        if command[0] == 'front':
            if len(l) == 0:
                print(-1)
            else:
                print(l[0])
        elif command[0] == 'back':
            if len(l) == 0:
                print(-1)
            else:
                print(l[-1])
        elif command[0] == 'size':
            print(len(l))
        elif command[0] == 'pop':
            if len(l) == 0:
                print(-1)
            else:
                print(l.popleft())
        else:
            if len(l) == 0:
                print(1)
            else:
                print(0)
    else:
        l.append(command[1])
