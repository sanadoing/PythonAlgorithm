N = int(input())

building = list(int(input()) for _ in range(N))
stack = []
result = 0

stack.append(building[0])

for i in range(1, N):

    print(stack)
    while True:
        if len(stack) > 0 and stack[-1] <= building[i]:
            stack.pop()
        else:
            break

    print(stack)
    result += len(stack)
    stack.append(building[i])

print(result)
#
# for i in range(N - 2, -1, -1):
#
#     if stack[-1] < building[i]:
#         result += len(stack)
#         stack.append(building[i])
#     elif i > 0 and building[i - 1] < max(stack) and stack[-1] >= building[i]:
#         stack.clear()
#         stack.append(building[i])
#     else:
#         stack.append(building[i])
#
# print(result)
