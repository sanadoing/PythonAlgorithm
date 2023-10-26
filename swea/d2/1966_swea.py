T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    #   버블 정렬
    while True:
        cnt = 0
        for i in range(N - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                cnt += 1

        if cnt == 0:
            break
    print(f'#{test_case}', end=' ')
    print(' '.join(map(str, numbers)))
