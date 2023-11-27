from collections import defaultdict


def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited))
            return

N = int(input())
graph = defaultdict(list)
for i in range(1,N+1):
    v = int(input())
    graph[v].append(i)

result = []
checked = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
for x in result:
    print(x)
