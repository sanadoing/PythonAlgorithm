import heapq
import sys

input = sys.stdin.readline

city = int(input())
bus = int(input())
graph = [[] for _ in range(city + 1)]

for _ in range(bus):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())


def dijkstra(start):
    costs = [sys.maxsize] * (city + 1)
    costs[start] = 0
    queue = []
    heapq.heappush(queue, (start, costs[start]))

    while queue:
        current_node, current_cost = heapq.heappop(queue)

        if costs[current_node] < current_cost:
            continue

        for next_node, next_cost in graph[current_node]:
            temp_cost = current_cost + next_cost
            if temp_cost < costs[next_node]:
                costs[next_node] = temp_cost
                heapq.heappush(queue, [next_node, temp_cost])

    return costs[end]


print(dijkstra(start))
