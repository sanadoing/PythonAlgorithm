N, M = map(int, input().split())
basket = [0] * (N + 1)

for _ in range(M):
    start, end, num = map(int, input().split())
    for i in range(start, end + 1):
        basket[i] = num

print(' '.join(map(str, basket[1:])))
