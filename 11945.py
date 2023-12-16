n, m = map(int, input().split())
bread = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m-1, -1, -1):
        print(bread[i][j], end='')
    print()