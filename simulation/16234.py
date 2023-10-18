dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0
while True:
    team = [[0] * N for _ in range(N)]  # 연합한 상태를 저장할 리스트
    team_number = 0
    team_cnt = dict()  # {team_number : [total, cnt]}
    for y in range(N):
        for x in range(N):
            for i in range(4):
                yy, xx = y + dy[i], x + dx[i]
                if 0 <= yy < N and 0 <= xx < N and L <= abs(board[y][x] - board[yy][xx]) <= R:
                    if team[y][x] == 0 and team[y][x] == team[yy][xx]:  # 두 나라 모두 연합이 없을 때
                        team_number += 1
                        team[y][x], team[yy][xx] = team_number, team_number
                        team_cnt[team_number] = [board[y][x] + board[yy][xx], 2]

                    elif team[y][x] != 0 and team[y][x] == team[yy][xx]:    # 두 나라 모두 같은 연합일 때, 각각 4방향으로 다 탐색하므로
                        continue
                    else:   # 두 나라 중 하나만 연합이 있을 때
                        if team[y][x] > team[yy][xx]:   # (y, x) 나라만 연합이 있을 때
                            team[yy][xx] = team[y][x]
                            team_cnt[team[y][x]] = [team_cnt[team[y][x]][0] + board[yy][xx],
                                                    team_cnt[team[y][x]][1] + 1]
                        else:    # (yy, xx) 나라만 연합이 있을 때
                            team[y][x] = team[yy][xx]
                            team_cnt[team[yy][xx]] = [team_cnt[team[yy][xx]][0] + board[y][x],
                                                      team_cnt[team[yy][xx]][1] + 1]


    if len(team_cnt) == 0:
        print(result)
        break

    for y in range(N):
        for x in range(N):
            if team[y][x] != 0:
                board[y][x] = team_cnt[team[y][x]][0] // team_cnt[team[y][x]][1]

    result += 1
