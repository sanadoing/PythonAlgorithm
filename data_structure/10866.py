from collections import deque
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())

    D = []
    D = deque(D)
    answer = []
    for _ in range(n):
        temp = input()
        if "push_front" in temp:
            temp, x = map(str, temp.split())
            D.appendleft(int(x))
        elif "push_back" in temp:
            temp, x = map(str, temp.split())
            D.append(int(x))
        elif "pop_front" in temp:
            if len(D) == 0:
                answer.append(-1)
            else:
                answer.append(D.popleft())

        elif "pop_back" in temp:
            if len(D) == 0:
                answer.append(-1)
            else:
                answer.append(D.pop())
        elif "size" in temp:
            answer.append(len(D))
        elif "empty" in temp:
            if len(D) == 0:
                answer.append(1)
            else:
                answer.append(0)
        elif "front" in temp:
            if len(D) == 0:
                answer.append(-1)
            else:
                answer.append(list(D)[0])

        else:
            if len(D) == 0:
                answer.append(-1)
            else:
                answer.append(list(D)[-1])

    print(*answer, sep = '\n')
    # for i in range(len(answer)):
    #     print(answer[i])