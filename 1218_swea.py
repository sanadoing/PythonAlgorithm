T = 10
for test_case in range(1, T + 1):
    N = int(input())
    string = input()
    stack = []

    for s in string:
        if s == '{' or s == '[' or s == '(' or s == '<':
            stack.append(s)
        else:
            temp = stack.pop()
            if s == '}' and temp != '{':
                print(f"#{test_case} 0")
                break
            elif s == ')' and temp != '(':
                print(f"#{test_case} 0")
                break
            elif s == ']' and temp != '[':
                print(f"#{test_case} 0")
                break
            elif s == '>' and temp != '<':
                print(f"#{test_case} 0")
                break
            else:
                continue

    else:
        print(f"#{test_case} 1")
