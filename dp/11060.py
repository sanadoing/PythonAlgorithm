from collections import deque

N = int(input())
board = list(map(int, input().split()))
visited = [0] * N
queue = deque([])

if N == 1:
    print(0)
else:
    for i in range(1, board[0] + 1):
        queue.append((0, i, 0))  # 출발점, 움직일 칸 수, 점프 수
    visited[0] = 1

    while queue:
        # print(queue)
        # print(visited)
        start_point, move, jump_cnt = queue.popleft()

        if start_point == N - 1:
            print(jump_cnt)
            break

        end = (start_point + move if start_point + move < N else N - 1)

        for i in range(end, start_point - 1, -1):

            if visited[i] == 0:
                visited[i] = 1
                queue.append((i, board[i], jump_cnt + 1))  # 출발점, 움직일 칸 수, 점프 수

    else:
        print(-1)
