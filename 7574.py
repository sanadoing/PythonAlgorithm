from collections import deque

n, r = map(int, input().split())
leaves = []
check = [0] * (n)

for i in range(n):
    x, y = map(int, input().split())
    leaves.append([(x, y), (x + r, y + r), i])
d = int(input())
queue = deque([])
queue.append(leaves[0])
result = -1
check[0] = 1
while queue:
    small, big, idx = queue.popleft()
    check[idx] = 1
    result = max(result, big[0]+big[1])
    for i in range(len(leaves)):
        leaf = leaves[i]
        if check[i] == 0:
            if (abs(big[0]-leaf[0][0]) or abs(big[1] - leaf[0][1]) or abs(small[0]-leaf[1][0]) or abs(small[1] - leaf[1][1])) <= d:
                print(small, leaf[0])
                queue.append(leaves[i])

print(result)