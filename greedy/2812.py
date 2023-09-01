N, K = map(int, input().split())
num = list(map(int, input()))
stack = [num[0]]

for i in range(1, len(num)):

    while len(stack) > 0 and K > 0:
        if stack[-1] < num[i]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(num[i])

if K > 0:
    print(''.join(map(str, stack[:-K])))
else:
    print(''.join(map(str, stack)))
