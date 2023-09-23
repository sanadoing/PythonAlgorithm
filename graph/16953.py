from collections import deque

A, B = map(int, input().split())
queue = deque([(A, 1)])

while queue:
    now, cnt = queue.popleft()
    if now * 2 == B or now * 10 + 1 == B:
        print(cnt + 1)
        break
    else:
        if now * 2 < B:
            queue.append((now * 2, cnt + 1))
        if now * 10 + 1 < B:
            queue.append((now * 10 + 1, cnt + 1))
else:
    print(-1)