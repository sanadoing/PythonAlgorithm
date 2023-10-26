T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    flag = False
    cnt, buy, result = 0, 0, 0
    max_price = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if max_price > arr[i]:
            buy += arr[i]
            cnt += 1
        else:
            result += max_price * cnt - buy
            cnt, buy = 0, 0
            max_price = arr[i]
    if cnt:
        result += max_price * cnt - buy

    print(f'#{test_case} {result}')
