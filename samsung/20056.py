dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())  # N: 격자 크기, M: 파이어볼 갯수, K: 명령 횟수

#   fireball[i][0]: i번째 파이어볼의 행 (r)
#   fireball[i][1]: i번째 파이어볼의 열 (c)
#   fireball[i][2]: i번째 파이어볼의 질량 (m)
#   fireball[i][3]: i번째 파이어볼의 속력 (s)
#   fireball[i][4]: i번째 파이어볼의 방향 (d)

fireball = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

board = [[0] * N for _ in range(N)]
#   board_info[(r, c)] = [cnt, m, s, d]
#   파이어볼의 위치 r행, c열
#   하나의 칸에 존재하는 파이어볼들의 갯수(cnt), 하나의 칸에 존재하는 파이어볼들의 질량 합(m),
#   하나의 칸에 존재하는 파이어볼들의 속력 합(s), 하나의 칸에 존재하는 파이어볼들의 방향의 방향이 같은지 다른지에 관한 수 (0: 다 짝수, 1: 다 홀수, 3: 방향 다름, 4: 리셋 값)
board_dic = [[0] * N for _ in range(N)]
board_info = dict()
result = 0


def board_add(r, c, m, s, d):
    global board_info

    if board_info.get((r, c), [0, 0, 0, 0]) == [0, 0, 0, 0]:

        board_info[(r, c)] = [1, m, s, d % 2]
    elif board_info[(r, c)] == [0, 0, 0, 4]:

        board_info[(r, c)] = [1, m, s, d % 2]
    else:

        board_info[(r, c)][0] += 1
        board_info[(r, c)][1] += m
        board_info[(r, c)][2] += s

        if board_info[(r, c)][3] != d % 2 and board_info[(r, c)][3] != 4:
            board_info[(r, c)][3] = 3
        elif board_info[(r, c)][3] == 4:
            board_info[(r, c)][3] = d % 2
        elif board_info[(r, c)][3] == d % 2:
            board_info[(r, c)][3] = d % 2


# def board_remove(r, c):
#     global board_info
#     board_info[(r, c)] = [0, 0, 0, 4]


#   제일 처음 주어진 파이어볼에 대해 정보 입력
for f in fireball:
    board[f[0]][f[1]] += 1  # board 칸의 파이어볼 갯수 + 1
    board_dic[f[0]][f[1]] = f[4]
    board_add(f[0], f[1], f[2], f[3], f[4])

while K:

    #   모든 파이어볼 자신의 방향과 속력만큼 이동
    for f in fireball:
        board[f[0]][f[1]] -= 1

        f[0] = ((f[0]) + dy[f[4]] * f[3]) % N
        f[1] = ((f[1]) + dx[f[4]] * f[3]) % N

        board[f[0]][f[1]] += 1
        board_dic[f[0]][f[1]] = f[4]
        board_add(f[0], f[1], f[2], f[3], f[4])

    fireball.clear()
    for y in range(N):
        for x in range(N):
            #   같은 칸에 파이어볼이 2개 이상이며, 합쳐진 파이어볼의 질량의 합/5가 0보다 큰 경우 => 4개의 파이어볼로 분해

            if (y, x) not in board_info:
                board[y][x] = 0
            elif board[y][x] > 1:

                if (board_info[(y, x)][1] // 5 > 0) and (board_info[(y, x)][3] != 4):

                    # 합쳐진 파이어볼의 방향이 홀, 짝이 달랐을 때
                    if board_info[(y, x)][3] == 3:
                        for i in range(4):
                            fireball.append(
                                [y, x, board_info[(y, x)][1] // 5, board_info[(y, x)][2] // board_info[(y, x)][0],
                                 i * 2 + 1])
                        #   합쳐진 파이어볼의 방향이 홀홀홀 이거나 짝짝짝으로 같았을 때
                        board[y][x] = 4
                    else:
                        for i in range(4):
                            fireball.append(
                                [y, x, board_info[(y, x)][1] // 5, board_info[(y, x)][2] // board_info[(y, x)][0],
                                 i * 2])
                        board[y][x] = 4

            elif board[y][x] == 1 and board_info[(y, x)][1] > 0:
                fireball.append([y, x, board_info[(y, x)][1], board_info[(y, x)][2], board_dic[y][x]])
                board[y][x] = 1

    board_info.clear()

    K -= 1

for f in fireball:
    result += f[2]

print(result)
