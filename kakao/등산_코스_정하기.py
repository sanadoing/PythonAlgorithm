from collections import defaultdict
from heapq import heappush, heappop


def solution(n, paths, gates, summits):
    summits.sort()
    set_summit = set(summits)
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))

    hq = []
    visited = [10000001] * (n + 1)
    # set_gates = set(gates)
    for gate in gates:
        heappush(hq, (0, gate))
        visited[gate] = 0

    while hq:
        intensity, node = heappop(hq)
        if intensity > visited[node] or node in set_summit:
            continue

        for weight, next_node in graph[node]:
            next_intensity = max(weight, intensity)
            if next_intensity < visited[next_node]:
                visited[next_node] = next_intensity
                heappush(hq, (next_intensity, next_node))

    min_intensity = [0, 10000001]
    for summit in summits:
        if min_intensity[1] > visited[summit]:
            min_intensity[0] = summit
            min_intensity[1] = visited[summit]

    return min_intensity