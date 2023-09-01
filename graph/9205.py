# from collections import deque
#
# t = int(input())
# dx = [-50, 50]
# dy = [-50, 50]
#
# for _ in range(t):
#     market, house, festival = [], [], []
#     market_cnt = int(input())
#
#     x, y = map(int, input().split())
#     house.append((x, y))
#
#     for _ in range(market_cnt):
#         x, y = map(int, input().split())
#         market.append((x, y))
#
#     x, y = map(int, input().split())
#     festival.append((x, y))
#
#     bear = 20
#     queue = deque([(house[0][0], house[0][1], bear)])
#     dic = dict()  # 방문 했던 곳인지 구분하기 위해
#
#     while queue:
#         x, y, bear = queue.popleft()
#
#         # 페스티벌에 도착
#         if x == festival[0][0] and y == festival[0][1]:
#             print("happy")
#             break
#         # 편의점에서 맥주 삼
#         if (x, y) in market:
#             bear = 20
#         # 맥주가 없을 경우 더 이상 이동 불가
#         if bear < 1:
#             continue
#         # x 값 -50m, +50m 이동
#         for i in range(2):
#             xx = x + dx[i]
#             if -32768 <= xx < 32767 and -32768 <= y < 32767 and dic.get((xx, y, bear - 1), 0) == 0:
#                 queue.append((xx, y, bear - 1))
#                 dic[(xx, y, bear - 1)] = 1
#         # y 값 -50m, +50m 이동
#         for i in range(2):
#             yy = y + dy[i]
#             if -32768 <= x < 32767 and -32768 <= yy < 32767 and dic.get((x, yy, bear - 1), 0) == 0:
#                 queue.append((x, yy, bear - 1))
#                 dic[(x, yy, bear - 1)] = 1
#
#     else:
#         print("sad")


from collections import deque


t = int(input())

for _ in range(t):
    market, house, festival = [], [], []
    market_cnt = int(input())

    x, y = map(int, input().split())
    house.append((x, y))

    for _ in range(market_cnt):
        x, y = map(int, input().split())
        market.append((x, y))

    x, y = map(int, input().split())
    festival.append((x, y))

    queue = deque([(house[0][0], house[0][1])])
    visited = [0] * market_cnt
    dic = dict()  # 방문 했던 곳인지 구분하기 위해

    while queue:
        x, y = queue.popleft()

        if abs(x-festival[0][0]) + abs(y-festival[0][1]) <= 1000:
            print("happy")
            break
        else:
            for i in range(market_cnt):
                if abs(x-market[i][0]) + abs(y-market[i][1]) <= 1000 and visited[i] == 0:
                    visited[i] = 1
                    queue.append((market[i][0], market[i][1]))

    else:
        print("sad")