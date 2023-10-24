T = int(input())
for test_case in range(1, T + 1):
    flag = 0
    board = [list(map(int, input().split())) for _ in range(9)]
    y = 0

    for i in range(9):
        row, box, x = 0, 0, i % 3
        column = sum(board[i])
        for j in range(9):
            row += board[j][i]
        for j in range(3):
            box += sum(board[y+j][x*3:x*3+3])
        if i == 2 or i == 5:
            y += 3
        if column != 45 or row != 45 or box != 45:
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} 1')