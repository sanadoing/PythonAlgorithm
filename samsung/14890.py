N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 가로 길 탐색
for y in range(N):
    cnt = 1
    for x in range(1, N):
        if board[y][x] == board[y][x - 1]:
            cnt += 1
            # 1칸 오르막
        elif board[y][x] - board[y][x - 1] == 1 and cnt >= 0:

            if cnt >= L:
                cnt = 1
            else:
                break
            # 1칸 내리막
        elif board[y][x - 1] - board[y][x] == 1 and cnt >= 0:
            cnt = 1 - L
        else:
            break
    else:
        if cnt >= 0:
            result += 1


for x in range(N):
    cnt = 1
    for y in range(1, N):
        if board[y][x] == board[y - 1][x]:
            cnt += 1
        elif board[y][x] - board[y - 1][x] == 1 and cnt >= 0:
            if cnt >= L:
                cnt = 1
            else:
                break
        elif board[y - 1][x] - board[y][x] == 1 and cnt >= 0:
            cnt = 1 - L
        else:
            break
    else:
        if cnt >= 0:
            result += 1

print(result)
