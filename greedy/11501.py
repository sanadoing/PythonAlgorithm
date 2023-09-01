T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    result = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max_num:
            max_num = arr[i]
        else:
            result += max_num-arr[i]
        print(arr[i], max_num, result)
    print(result)