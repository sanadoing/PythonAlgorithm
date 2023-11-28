import heapq

INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
result = -1

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([c, e])

def dijkstra(s):
    queue = []
    heapq.heappush(queue, [0, s])
    distance = [INF] * (N + 1)
    distance[s] = 0

    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for v in graph[node]:
            next_cost = cost + v[0]
            if distance[v[1]] > next_cost:
                distance[v[1]] = next_cost
                heapq.heappush(queue, [next_cost, v[1]])
    return distance

back = dijkstra(X)
for i in range(1, N + 1):
    go = dijkstra(i)
    result = max(result, go[X] + back[i])

print(result)
