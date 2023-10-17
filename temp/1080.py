M, N = map(int, input().split())
A = [list(map(int, input())) for _ in range(M)]
B = [list(map(int, input())) for _ in range(M)]
result = 0

for i in range(M - 2):
    for j in range(N - 2):
        if A[i][j] != B[i][j]:

            for k in range(3):
                for o in range(3):
                    if A[i + k][j + o] == 1:
                        A[i + k][j + o] = 0
                    else:
                        A[i + k][j + o] = 1
            result += 1


for i in range(M):
    if A[i] != B[i]:
        print(-1)
        break
else:
    print(result)