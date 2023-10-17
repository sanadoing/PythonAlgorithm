mine = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
zero_cnt = [[0] * 5 for _ in range(2)]
cross1 = 0
cross2 = 0
result = 0

for i in range(5):
    for j in range(5):
        zero_cnt[0][i] += mine[i][j]
        zero_cnt[1][j] += mine[i][j]
        if i == j:
            cross1 += mine[i][j]
        if (i, j) == ((2, 2) or (3, 1) or (1, 3) or (0, 4) or (4, 0)):
            cross2 += mine[i][j]

for i in range(5):
    for j in range(5):
        for m in range(5):
            if mc[i][j] in mine[m]:
                print(i, j)
                zero_cnt[0][m] -= mc[i][j]
                zero_cnt[1][mine[m].index(mc[i][j])] -= mc[i][j]

                if m == mine[m].index(mc[i][j]):
                    print("cross1", m, mine[m].index(mc[i][j]))
                    cross1 -= mc[i][j]
                if (m, mine[m].index(mc[i][j])) == ((2, 2) or (3, 1) or (1, 3) or (0, 4) or (4, 0)):
                    print("cross2", m, mine[m].index(mc[i][j]))
                    cross2 -= mc[i][j]

        result += 1
        zero = 0

        for z in range(2):
            zero += zero_cnt[z].count(0)

        if cross1 == 0:
            zero += 1
        if cross2 == 0:
            zero += 1

        for z in range(2):
            print(zero_cnt[z])
        print(cross1, cross2)
        if zero >= 3:
            print(result)
            exit(0)
