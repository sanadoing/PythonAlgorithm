N, K = map(int, input().split())
idx = 0

for i in range(1, N + 1):
    if N % i == 0:
        idx += 1
    if idx == K:
        print(i)
        break
else:
    print(0)
