T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    max_n, min_n = max(numbers), min(numbers)
    print(f'#{test_case} {round((sum(numbers)-max_n-min_n)/8)}')