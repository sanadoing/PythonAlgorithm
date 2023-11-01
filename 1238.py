N, M, X = map(int, input().split())
dic = dict()
result = -int(1e9)

def go(n, t):
    global visited, temp_go
    if n == X:
        temp_go = min(temp_go, t)
    if visited[n - 1] == 0:
        for a, b in dic[n]:
            visited[n - 1] = 1
            go(a, t + b)

def come(n, home, t):
    global visited, temp_come
    if n == home:
        temp_come = min(temp_come, t)
    if visited[n - 1] == 0:
        for a, b in dic[n]:
            visited[n - 1] = 1
            come(a, home, t + b)


for _ in range(M):
    s, e, t = map(int, input().split())
    if dic.get(s, (0, 0)) == (0, 0):
        dic[s] = [(e, t)]
    else:
        dic[s].append((e, t))

for i in range(1, N + 1):
    temp_go = int(1e9)
    temp_come = int(1e9)

    visited = [0] * N
    go(i, 0)
    visited = [0] * N
    come(X, i, 0)
    if temp_go + temp_come > result:
        result = temp_go + temp_come

print(result)
