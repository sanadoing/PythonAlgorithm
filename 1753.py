import heapq

V, E = map(int, input().split())
K = int(input())
dp = [1e9] * (V + 1)
heap = []
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (start, 0))

    while heap:
        now_node, now_cost = heapq.heappop(heap)

        if dp[now_node] < now_cost:
            continue
        for next_node, next_cost in graph[now_node]:
            next_cost = next_cost + now_cost
            if next_cost < dp[next_node]:
                dp[next_node] = next_cost
                heapq.heappush(heap, (next_node, next_cost))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if dp[i] == 1e9 else dp[i])