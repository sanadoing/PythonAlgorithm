T = int(input())


def is_promising(d):
    for i in range(d):
        if row[d] == row[i] or abs(row[d] - row[i]) == abs(d - i):
            return False
    return True


def N_queen(depth):
    global result, row, N
    if depth == N:
        result += 1
    else:
        for i in range(N):
            row[depth] = i
            if is_promising(depth):
                N_queen(depth + 1)


for test_case in range(1, T + 1):
    N = int(input())
    row = [0] * N
    result = 0
    N_queen(0)
    print(f'#{test_case} {result}')
