from collections import deque, defaultdict

n = int(input())
buildings = defaultdict(list)
queue = deque([])
buildings_info = [0] * (n+1)
result = [0] * (n+1)
for i in range(n):
    b = list(map(int, input().split()))
    if len(b) == 2:
        queue.append(i + 1)
        result[i+1] = b[0]
    else:
        buildings[b[1]].append(i+1)
    buildings_info[i+1] = b[0]
while queue:
    n = queue.popleft()
    for b in buildings[n]:
        result[b] = buildings_info[b] + result[n]
        if b in buildings:
            queue.append(b)

for i in range(1, len(buildings_info)):
    print(result[i])
