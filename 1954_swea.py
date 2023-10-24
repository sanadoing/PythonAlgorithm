dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    y, x = 0, 0
    direction = 0  # 맨 처음 오른쪽 방향
    result = [[0] * N for _ in range(N)]
    for i in range(1, N * N + 1):
        result[y][x] = i

        if i == N * N:
            break
        while True:
            yy, xx = y + dy[direction], x + dx[direction]
            if 0 <= yy < N and 0 <= xx < N and result[yy][xx] == 0:
                break
            else:
                direction = (direction + 1) % 4

        y, x = y + dy[direction], x + dx[direction]

    print(f'#{test_case}')
    for r in result:
        print(' '.join(map(str, r)))
