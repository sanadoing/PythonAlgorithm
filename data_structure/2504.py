a = list(map(str, input()))

stack = []
result = 0
temp = 1

for i in range(len(a)):

    if a[i] == '(':
        temp *= 2
        stack.append(a[i])

    elif a[i] == '[':
        temp *= 3
        stack.append(a[i])

    elif a[i] == ')':

        if not stack or stack[-1] != '(':
            result = 0
            break

        if a[i-1] == '(':
            result += temp

        temp //= 2
        stack.pop()

    elif a[i] == ']':

        if not stack or stack[-1] != '[':
            result = 0
            break

        if a[i-1] == '[':
            result += temp

        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
