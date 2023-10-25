T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(str, input()))
    result = 0
    for i in range(1, len(arr) + 1):
        if arr[0:i] == arr[i:i * 2]:
            result = i
            break
    print(f'#{test_case} {result}')
