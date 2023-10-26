T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(N):
        flag1, cnt1 = False, 0
        for x in range(N):
            if board[y][x] == 1:
                cnt1 += 1
            else:
                if flag1:
                    result += 1
                cnt1, flag1 = 0, False
            if cnt1 == K:
                flag1 = True
            elif cnt1 > K:
                flag1 = False

        if cnt1 == K:
            result += 1

        flag2, cnt2 = False, 0
        for x in range(N):
            if board[x][y] == 1:
                cnt2 += 1
            else:
                if flag2:
                    result += 1
                cnt2, flag2 = 0, False
            if cnt2 == K:
                flag2 = True
            elif cnt2 > K:
                flag2 = False
        if cnt2 == K:
            result += 1

    print(f'#{test_case} {result}')
