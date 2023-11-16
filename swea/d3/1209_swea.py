for _ in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    result = -1
    temp1, temp2 = 0, 0
    for i in range(100):
        x_sum = sum(board[i][:])
        y_sum = 0
        for j in range(100):
            y_sum += board[j][i]
        result = max(result, x_sum, y_sum)
        temp1 += board[i][i]
        temp2 += board[i][99-i]
    result = max(result, temp1, temp2)
    print(f'#{N} {result}')
