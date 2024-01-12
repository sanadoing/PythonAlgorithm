# 위(0), 오(1), 아(2), 왼(3) 
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

s1 = [3, 2, 1, 0]    # \
s2 = [1, 0, 3, 2]    # /
    

n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]
rocket = list(map(int, input().split()))
result = [0, 0, 0, 0]    # U, R, D, L

for b in board:
    print(b)
def go(y, x, d):
    visited = [[0] * m for _ in range(n)]
    visited[y][x] = 1
    cnt = 0
    
    while True:
        yy, xx = y+ dy[d], x + dx[d]
        if 0 <= yy < n and 0 <= xx < m :
            if visited[yy][xx] == 0:
                if board[yy][xx] == 'C':
                    return cnt + 1
                elif board[yy][xx] == '\':
                    cnt += 1
                    d = s1[d]
                elif board[yy][xx] == '/':
                    cnt += 1
                    d = s2[d]
            else:    # 무한히 전파 될 수 있는 경우 
                return 'Voyager'

        else:    # 항성계를 벗어남 
            return cnt + 1
    
for i in range(4):
    yy, xx = rocket[0] + dy[i] -1, rocket[1] + dx[i] -1
    if 0 <= yy < n and 0<=xx<m :
        result[i] = go(yy, xx, i)

for i in range(4):
    if result[i]
