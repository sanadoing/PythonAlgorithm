T = int(input())

def dfs(cnt, s):

    global result
    flag = True
    for i in range(10):
        if visited[i] == 0 and board[s][i] == 1:
            visited[i] = 1
            result = max(result, cnt+1)
            dfs(cnt+1, i)
            visited[i] = 0
            flag = False

    if flag:
        return



for _ in range(T):
    N, M = map(int, input().split())
    board = [[0] * 10 for _ in range(10)]
    visited = [0] * 10
    routes = []
    result = 0
    for _ in range(M):
        a, b = map(int, input().split())
        board[a][b] = 1
        board[b][a] = 1
        routes.append([a, b])
        routes.append([b, a])
    for i in range(len(routes)):
        s, e = routes[i][0], routes[i][1]
        visited[s] = 1
        result = 1
        dfs(1, e)
    print(result)


