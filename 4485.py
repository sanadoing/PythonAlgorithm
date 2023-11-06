import heapq

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

count = 1


def dijkstra():
    global count
    queue = []
    heapq.heappush(queue, (board[0][0], 0, 0))  # cost, y, x
    distance[0][0] = 0

    while queue:
        cost, y, x = heapq.heappop(queue)

        if y == N - 1 and x == N - 1:
            print(f'Problem {count}: {distance[y][x]}')
            count += 1
            return

        for i in range(4):
            yy, xx = y + dy[i], x + dx[i]
            if 0 <= yy < N and 0 <= xx < N:
                new_cost = cost + board[yy][xx]
                if new_cost < distance[yy][xx]:
                    distance[yy][xx] = new_cost
                    heapq.heappush(queue, (new_cost, yy, xx))


while True:
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    distance = [[int(1e9)] * N for _ in range(N)]
    dijkstra()
