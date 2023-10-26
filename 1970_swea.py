money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    now = N

    print(f"#{test_case}")
    for i in range(8):
        if money[i] <= now:
            print(now // money[i], end=' ')
            now = now % money[i]
        else:
            print(0, end=' ')

    print()