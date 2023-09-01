if __name__ == "__main__":

    str = input()
    bomb = input()
    stack = []

    for i in range(len(str)):
        stack.append((str[i]))
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

    if len(stack) == 0:
        print("FRULA")
    else:
        print(''.join(stack))
