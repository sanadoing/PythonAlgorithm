def DFS(depth, idx):
    global result
    if depth == N // 2:
        team1, team2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += board[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += board[i][j]
        result = min(result, abs(team1 - team2))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            DFS(depth + 1, i + 1)
            visited[i] = False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)
visited = [False for _ in range(N)]
DFS(0, 0)
print(result)
