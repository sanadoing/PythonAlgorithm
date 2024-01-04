y, x = map(int, input().split())
numbers = [[0] * x for _ in range(y)]
for _ in range(2):
    for i in range(y):
        ns = list(map(int, input().split()))
        for j in range(x):
            numbers[i][j] += ns[j]
for i in range(y):
    print(' '.join(map(str, numbers[i])))