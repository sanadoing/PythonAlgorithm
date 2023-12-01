import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
dist = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    heapq.heappush(dist[1], 0)
    while q:
        distance, now = heapq.heappop(q)

        for next_distance, next_node in graph[now]:
            cost = distance + next_distance

            if (len(dist[next_node]) <= K):
                heapq.heappush(q, (cost, next_node))
                heapq.heappush(dist[next_node], -cost)
            else:
                if (dist[next_node][0] < -cost):
                    heapq.heappop(dist[next_node])
                    heapq.heappush(q, (cost, next_node))
                    heapq.heappush(dist[next_node], -cost)


dijkstra()

for idx in range(1, N + 1):
    if len(dist[idx]) < K:
        print("-1")
    else:
        dist[idx].sort()
        print(-dist[idx][-K])
