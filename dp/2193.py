
N = int(input())
f = [0] * (N + 1)

if N > 2:
    f[1], f[2] = 1, 1
    idx = 3
    while True:
        f[idx] = f[idx - 1] + f[idx - 2]
        if idx == N:
            print(f[idx])
            break
        idx += 1
else:
    print(1)
