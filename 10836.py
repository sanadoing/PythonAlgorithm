import sys
input = sys.stdin.readline
M, N = map(int, input().split())
bees = [[1] * M for _ in range(M)]
grow = [1] * (2 * M - 1)
for _ in range(N):
    z, o, t = map(int, input().split())
    for idx in range(z, z+o):
        grow[idx] += 1
    for idx in range(z+o, z+o+t):
        grow[idx] += 2
for idx in range(M - 1, -1, -1):
    print(' '.join(map(str, [grow[idx]] + grow[M:])))

