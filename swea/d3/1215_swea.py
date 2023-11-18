for test_case in range(1, 11):
    l = int(input())
    board = [list(map(str, input())) for _ in range(8)]
    result = 0
    for y in range(8):
        for i in range(9 - l):
            if l % 2 == 0:
                if board[y][i:i + (l // 2)] == list(reversed(board[y][i + (l // 2):i + l])):
                    result += 1
            else:
                if board[y][i:i + (l // 2)] == list(reversed(board[y][i + (l // 2) + 1:i + l])):
                    result += 1
            for j in range(l // 2):
                if board[i + j][y] != board[(l + i) - j - 1][y]:
                    break
            else:
                result += 1
    print(f'#{test_case} {result}')
