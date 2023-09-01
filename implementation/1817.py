from collections import deque

if __name__ == "__main__":
    N, M = map(int, input().split())

    cnt = 0

    if N == 0:
        cnt = 0
    else:
        book = list(map(int, input().split()))
        stack = []
        for b in book:
            stack.append(b)

            if sum(stack) < M:
                continue
            elif sum(stack) == M:
                stack.clear()
                cnt += 1
            else:
                stack.clear()
                stack.append(b)
                cnt += 1
        if sum(stack) > 0:
            cnt += 1

    print(cnt)
