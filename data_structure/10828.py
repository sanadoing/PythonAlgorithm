import sys
if __name__ == "__main__":
    n = int(input())
    stack = []
    answer = ''
    for _ in range(n):
        str1 = input()
        if str1[:2] == "pu":
            str1, str2 = str1.split()
            stack.append(str2)
        elif str1 == "pop":
            if len(stack) == 0:
                answer += '-1' + '\n'
                # print(-1)
            else:
                answer += stack.pop() + '\n'
                # print(stack.pop())
        elif str1 == "size":
            answer += str(len(stack)) + '\n'
            # print(len(stack))
        elif str1 == "empty":
            if len(stack) == 0:
                answer += '1' + '\n'
                # print(1)
            else:
                answer += '0' + '\n'
                # print(0)
        else:
            if len(stack) == 0:
                answer += '-1' + '\n'
                # print(-1)
            else:
                answer += stack[-1] + '\n'
                # print(stack[-1])


    print(answer)
