N = int(input())
bear = list(map(str, input()))

stack = []
result = 0

for i in range(len(bear)):
    if len(stack) == 0 or stack[-1] == bear[i]:
        stack.append(bear[i])
    else:
        if len(stack) != 0:
            stack.pop()

    result = max(result, len(stack))

if len(stack) == 0:
    print(result)
else:
    print(-1)
