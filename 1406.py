import sys

input = sys.stdin.readline
stack1 = list(input().strip())
stack2 = []
N = int(input())
cursor = len(stack1)
for _ in range(N):
    command = input().split()
    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command[0] == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(command[1])
stack1.extend(reversed(stack2))
print(''.join(map(str, stack1)))
