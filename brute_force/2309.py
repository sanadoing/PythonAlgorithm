small = []

for _ in range(9):
    small.append(int(input()))


for i in range(9):
    sum_weight = sum(small)
    sum_weight -= small[i]

    for j in range(9):
        if i != j:
            sum_weight -= small[j]

            if sum_weight == 100:
                small[i] = 0
                small[j] = 0
                small.sort()
                print('\n'.join(map(str, small[2:])))
                exit(0)
            sum_weight += small[j]

    sum_weight += small[i]


