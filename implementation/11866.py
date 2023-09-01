from collections import deque

N, K = map(int, input().split())
l = list(i for i in range(1, N + 1))

result = []
l = deque(l)

while l:
    cnt = K - 1
    while cnt:
        l.append(l.popleft())
        cnt -= 1
    result.append(l.popleft())

print(f'<{", ".join(map(str, result))}>')
