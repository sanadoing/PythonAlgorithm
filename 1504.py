import heapq

N, E = map(int, input().split())
gragh = [[] for _ in range(N + 1)]


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [1e9] * (N + 1)
    distance[start] = 0
    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if distance[now_node] < now_cost:
            continue
        for cost, node in gragh[now_node]:
            next_cost = cost + now_cost
            if next_cost < distance[node]:
                distance[node] = next_cost
                heapq.heappush(heap, (next_cost, node))
    return distance

for _ in range(E):
    a, b, c = map(int, input().split())
    gragh[a].append((c, b))
    gragh[b].append((c, a))

v1, v2 = map(int, input().split())
# 1 에서 출발하는 최단 거리
first = dijkstra(1)
# v1 에서 출발하는 최단 거리
v1_v2 = dijkstra(v1)
# v2 에서 출발하는 최단 거리
v2_v1 = dijkstra(v2)

v1_route = first[v1] + v1_v2[v2] + v2_v1[N]
v2_route = first[v2] + v2_v1[v1] + v1_v2[N]

result = min(v1_route, v2_route)

print(result if result < int(1e9) else -1)
