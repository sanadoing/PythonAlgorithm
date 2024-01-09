import sys
input = sys.stdin.readline

n = int(input())
l = []
front, back, size = 0, -1, 0
for _ in range(n):
    command = list(map(str, input().split()))
    if len(command) == 1:
        if command[0] == 'front':
            if size == 0:
                print(-1)
            else:
                print(l[front])
        elif command[0] == 'back':
            if size == 0:
                print(-1)
            else:
                print(l[back])
        elif command[0] == 'size':
            print(size)
        elif command[0] == 'pop':
            if size == 0:
                print(-1)
            else:
                print(l[front])
                front += 1
                size -= 1
        else:
            if size == 0:
                print(1)
            else:
                print(0)
    else:
        l.append(command[1])
        size += 1
