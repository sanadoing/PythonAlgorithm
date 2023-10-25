T = int(input())
n = [2, 3, 5, 7, 11]
for test_case in range(1, T + 1):
    N = int(input())
    result = ''
    for i in range(5):
        now = N
        cnt = 0
        while now % n[i] == 0:
            now //= n[i]
            cnt += 1
        result += str(cnt)
    result = ' '.join(map(str, result))
    print(f'#{test_case} {result}')
