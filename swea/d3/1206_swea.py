for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        left = max(buildings[i-2:i])
        right = max(buildings[i+1:i+3])
        cnt = buildings[i] - max(left, right)
        if cnt > 0:
            result += cnt
    print(f'#{test_case} {result}')