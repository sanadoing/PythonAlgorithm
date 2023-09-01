from collections import deque

dx = [-1, 1, 2]  # +, +, *

N, K = map(int, input().split())
dic = dict()
cnt = 0

queue = deque()
queue.append((N, cnt))
dic[N] = 1

while queue:
    x, cnt = queue.popleft()

    if x == K:
        print(cnt)
        break
    #   걷기
    for i in range(2):
        xx = x + dx[i]
        if 0 <= xx <= 100000 and dic.get(xx, 0) == 0:
            dic[xx] = 1
            queue.append((xx, cnt + 1))

        #   순간 이동
    for _ in range(1):
        xx = x * dx[2]
        if 0 <= xx <= 100000 and dic.get(xx, 0) == 0:
            dic[xx] = 1
            queue.append((xx, cnt + 1))

