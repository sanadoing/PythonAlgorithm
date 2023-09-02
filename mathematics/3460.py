T = int(input())

for _ in range(T):
    result = []
    N = int(input())
    idx = 0

    while N > 0:
        if N % 2 == 1:
            result.append(idx)
        N = N // 2
        idx += 1

    print(' '.join(map(str, result)))
