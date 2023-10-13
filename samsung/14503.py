dy = [-1, 0, 1, 0]  # 북, 동, 남, 서
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
y, x, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:

    # 현재 칸이 청소가 되지 않은 경우 -> 청소 !
    if room[y][x] == 0:
        result += 1
        room[y][x] = 3  # 3은 청소를 완료한 칸

    else:
        dd = d
        # 현재 칸의 주변 4칸 탐색
        for _ in range(4):

            dd = (dd - 1) % 4  # 북,동,남,서를 +1이 아닌, -1로 -> 북,서,남,동 으로 반시계 90도로
            yy = y + dy[dd]
            xx = x + dx[dd]

            # 주변 4칸 중 청소 안한 칸이 있을 경우
            if 0 <= yy < N and 0 <= xx < M and room[yy][xx] == 0:
                room[yy][xx] = 3
                y = yy
                x = xx
                d = dd
                result += 1
                break
        # 현재 칸의 주변 4칸에 청소되지 않은 빈 칸이 없는 경우
        else:
            # 바라보는 방향을 유지한 채, 한 칸 '후진' 이므로
            # 나아가는 방향은 바라보는 방향의 반대가 된다. 북 <-> 남, 동 <-> 서 그렇기 때문에 -2
            dd = (d - 2) % 4
            yy = y + dy[dd]
            xx = x + dx[dd]

            if 0 <= yy < N and 0 <= xx < M:
                # 벽이라서 후진이 불가능한 경우 -> 작동 정지
                if room[yy][xx] == 1:
                    break
                else:
                    y = yy
                    x = xx

print(result)
