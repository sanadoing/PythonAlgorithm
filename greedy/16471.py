N = int(input())
mine = list(map(int, input().split()))
boss = list(map(int, input().split()))

mine.sort()
boss.sort()

m = 0
b = 0
win = 0

while m < N and b < N:
    if mine[m] < boss[b]:
        win += 1
        m += 1
        b += 1
    else:
        b += 1

if win >= (N + 1) // 2:
    print("YES")
else:
    print("NO")

