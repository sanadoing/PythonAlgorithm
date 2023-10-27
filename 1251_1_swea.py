T = int(input())


def link(start):
    distance[start] = 0

    for _ in range(N):
        min_value = int(1e9)
        min_idx = -1
        for i in range(N):
            if visited[i] == 0 and distance[i] < min_value:
                min_idx = i
                min_value = distance[i]

        visited[i] = 1


for test_case in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    tax = float(input())

    visited = [0] * N
    distance = [int(1e9)] * N

    link(0)
