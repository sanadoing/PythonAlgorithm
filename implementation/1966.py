from collections import deque

N = int(input())

for _ in range(N):
    C, M = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(enumerate(l1, start=0))
    l2 = deque(l2)
    cnt = 1
    while len(l2) > 0:
        idx, num = l2.popleft()

        if idx == M and num == max(l1):
            print(cnt)
            break
        elif num == max(l1):
            l1.remove(num)
            cnt += 1
        else:
            l2.append((idx, num))
