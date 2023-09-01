from collections import deque

if __name__ == "__main__":
    c = int(input())
    n = int(input())

    computer = [[0 for j in range(c + 1)] for i in range(c + 1)]

    for _ in range(n):
        x, y = map(int, input().split())
        computer[x][y] = 1
        computer[y][x] = 1

    queue = []
    queue = deque()
    queue.append(1)

    virus = []
    virus.append(1)

    while queue:
        pre_virus = queue.popleft()
        for i in range(c+1):
            if computer[pre_virus][i] == 1 and i not in virus:
                queue.append(i)
                virus.append(i)

    print(len(virus)-1)
