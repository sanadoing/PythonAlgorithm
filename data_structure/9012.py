T = int(input())
for _ in range(T):
    string = input()
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")