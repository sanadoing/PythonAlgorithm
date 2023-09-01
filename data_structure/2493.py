N = int(input())
num = list(map(int, input().split()))

stack = [(num[0], 1)]
result = [0]

for i in range(1, N):
    while True:
        if len(stack) == 0:
            result.append(0)
            break

        if stack[-1][0] < num[i]:
            stack.pop()
        else:
            result.append(stack[-1][1])
            break

    stack.append((num[i], i + 1))

print(' '.join(map(str, result)))