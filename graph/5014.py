from collections import deque

F, S, G, U, D = map(int, input().split())  # 전체 층수, 강호 층, 스타트링크 층, 위 버튼, 아래 버튼
dic = dict()
cnt = 0
queue = deque()
queue.append((S, cnt))
dic[S] = 1

while queue:
    now, cnt = queue.popleft()
    if now == G:
        print(cnt)
        break

    now_up = now + U
    if 1 <= now_up <= F and dic.get(now_up, 0) == 0:
        dic[now_up] = 1
        queue.append((now_up, cnt + 1))

    now_down = now - D
    if 1 <= now_down <= F and dic.get(now_down, 0) == 0:
        dic[now_down] = 1
        queue.append((now_down, cnt + 1))

else:
    print("use the stairs")