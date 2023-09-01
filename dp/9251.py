a = input()
b = input()
board = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            board[i + 1][j + 1] = board[i][j] + 1

        else:
            board[i + 1][j + 1] = max(board[i + 1][j], board[i][j + 1])

print(board[-1][-1])