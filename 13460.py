from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
board = []
red_ball = [0, 0]
blue_ball = [0, 0]
queue = deque()

for i in range(N):
    board.append(list(map(str, input())))
    for j in range(M):
        if board[i][j] == 'B':
            blue_ball[0] = i
            blue_ball[1] = j
            board[i][j] = '.'
        if board[i][j] == 'R':
            red_ball[0] = i
            red_ball[1] = j
            board[i][j] = '.'

queue.append([1, red_ball[0], red_ball[1], blue_ball[0], blue_ball[1]])
visited = [red_ball[0], red_ball[1], blue_ball[0], blue_ball[1]]

def game():
    while queue:
        cnt, r_y, r_x, b_y, b_x = queue.popleft()

        for i in range(4):
            nb_y, nb_x = b_y, b_x
            nr_y, nr_x = r_y, r_x

            # blue ball 이동
            while board[nb_y + dy[i]][nb_x + dx[i]] == '.':
                nb_y += dy[i]
                nb_x += dx[i]

            if board[nb_y + dy[i]][nb_x + dx[i]] == 'O':
                continue

            # red ball 이동
            while board[nr_y + dy[i]][nr_x + dx[i]] == '.':
                nr_y += dy[i]
                nr_x += dx[i]
            if board[nr_y + dy[i]][nr_x + dx[i]] == 'O':
                return cnt


            if nr_y == nb_y and nr_x == nb_x:
                if abs(b_x - nb_x) + abs(b_y - nb_y) < abs(r_x - nr_x) + abs(r_y - nr_y):
                    nr_y -= dy[i]
                    nr_x -= dx[i]
                else:
                    nb_y -= dy[i]
                    nb_x -= dx[i]

            if [nr_y, nr_x, nb_y, nb_x] not in visited:
                queue.append([cnt + 1, nr_y, nr_x, nb_y, nb_x])
                visited.append([nr_y, nr_x, nb_y, nb_x])

        if cnt > 10:
            return -1


    else:
        return -1

print(game())
