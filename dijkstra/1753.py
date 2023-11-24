import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
distance = [1e9] * (V + 1)
heap = []
graph = [[] for _ in range(V + 1)]

def dijkstra(start):
    distance[start] = 0
    heapq.heappush(heap, (0, start))    #   cost, node

    while heap:
        now_cost, now_node = heapq.heappop(heap)

        if distance[now_node] < now_cost:   #   현재 노드까지 오는 저장된 cost가 지금 값보다 이미 작을 경우
            continue
        for cost, next_node in graph[now_node]:
            next_cost = cost + now_cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1, V + 1):
    print("INF" if distance[i] == 1e9 else distance[i])
