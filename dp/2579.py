N = int(input())
stairs = list(int(input()) for _ in range(N))

result = [0] * N

if N > 2:
    result[0] = stairs[0]
    result[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        result[i] = max(result[i - 3] + stairs[i - 1] + stairs[i], result[i - 2] + stairs[i])

    print(result[N - 1])
else:
    print(sum(stairs))
