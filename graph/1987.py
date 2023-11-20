dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def dfs(y, x, c):
    global result
    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < R and 0 <= xx < C and visited[yy][xx] == 0:
            if alphabet[ord(board[yy][xx]) - 65] == 0:
                visited[yy][xx] = 1
                result = max(result, c + 1)
                alphabet[ord(board[yy][xx]) - 65] = 1
                dfs(yy, xx, c + 1)
                visited[yy][xx] = 0
                alphabet[ord(board[yy][xx]) - 65] = 0

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
alphabet = [0 for _ in range(26)]
result = 1
alphabet[ord(board[0][0]) - 65] = 1
visited =[[0] * C for _ in range(R)]
visited[0][0] = 1
cnt = 1
dfs(0, 0, cnt)
print(result)
