import sys
input = sys.stdin.readline
N = int(input())
stack = []
result = []
for _ in range(N):
    command = input().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if len(stack) > 0:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif command[0] == '3':
        result.append(len(stack))
    elif command[0] == '4':
        if len(stack) > 0:
            result.append(0)
        else:
            result.append(1)
    else:
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))
