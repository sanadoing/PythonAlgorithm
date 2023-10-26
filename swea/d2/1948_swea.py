days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

T = int(input())
for test_case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result, now_m, now_d = 0, m1, d1

    while now_m != m2:
        result += days[now_m] - now_d + 1
        now_m += 1
        now_d = 1

    result += d2 - now_d + 1
    print(f'#{test_case} {result}')
