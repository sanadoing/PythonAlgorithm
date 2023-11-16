T = int(input())
def DFS(point, cal, idx):
    global result
    for i in range(idx, N):
        if visited[i] == 0 and cal + foods[i][1] <= L:
            new_point = point + foods[i][0]
            new_cal = cal + foods[i][1]
            if check.get((new_point, new_cal), 1) == 1:
                visited[i] = 1
                check[(new_point, new_cal)] = 0
                result = max(result, point + foods[i][0])
                DFS(point + foods[i][0], cal + foods[i][1], i)
                visited[i] = 0

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    visited = [0] * N
    check = dict()
    DFS(0, 0, 0)
    print(f'#{test_case} {result}')
