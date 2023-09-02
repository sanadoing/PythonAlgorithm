import sys

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    temp = [0] * 3

    for i in range(3):
        for j in range(i, 10):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr[2])


    # temp.sort()
    # print(temp[7])
