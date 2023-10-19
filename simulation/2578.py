board = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]
result = 0
column = [0] * 5
row = [0] * 5
cross1 = 0
cross2 = 0
cross2_nums = [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]]

for i in range(5):
    for j in range(5):
        result += 1
        now_number = numbers[i][j]

        bingo_cnt = 0

        for b_y in range(5):
            for b_x in range(5):
                if board[b_y][b_x] == now_number:
                    column[b_y] += 1
                    row[b_x] += 1
                    if b_y == b_x:
                        cross1 += 1
                    if [b_y, b_x] in cross2_nums:
                        cross2 += 1
                        continue

        bingo_cnt += column.count(5)
        bingo_cnt += row.count(5)
        if cross1 == 5:
            bingo_cnt += 1
        if cross2 == 5:
            bingo_cnt += 1

        if bingo_cnt >= 3:
            print(result)
            exit(0)


