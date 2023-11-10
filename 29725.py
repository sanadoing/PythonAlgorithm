point = {'K': 0, 'k': 0, 'P': 1, 'p': 1, 'N': 3, 'n': 3, 'B': 3, 'b': 3, 'R': 5, 'r': 5, 'Q': 9, 'q': 9}
board = [list(map(str, input())) for _ in range(8)]
white, black = 0, 0
for y in range(8):
    for x in range(8):
        if board[y][x] != '.':
            if ord(board[y][x]) < 97:
                white += point[board[y][x]]
            else:
                black += point[board[y][x]]
print(white-black)
