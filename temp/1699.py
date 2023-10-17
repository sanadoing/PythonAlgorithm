import sys
N = int(input())
s = 1  # 제곱근이 될 수
square = s * s  # 제곱이 될 수
board = [sys.maxsize] * (N + 1)
board[0] = 0
while True:
    if square > N:
        print(board[N])
        break
    else:
        for i in range(square, N + 1):
            board[i] = min(board[i - square] + 1, board[i])

        s += 1
        square = s * s


