T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    apart = [[1] * (n+1) for _ in range(k+1)]
    for i in range(k+1):
        for j in range(2, n+1):
            if i == 0:
                apart[i][j] = j
            else:
                apart[i][j] = apart[i][j-1] + apart[i-1][j]
    print(apart[k][n])
