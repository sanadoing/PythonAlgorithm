import sys


def DFS(i, number):
    global add, minus, multi, div, max_num, min_num

    if i == N:
        max_num = max(number, max_num)
        min_num = min(number, min_num)

    else:
        if add > 0:
            add -= 1
            DFS(i + 1, number + num[i])
            add += 1
        if minus > 0:
            minus -= 1
            DFS(i + 1, number - num[i])
            minus += 1
        if multi > 0:
            multi -= 1
            DFS(i + 1, number * num[i])
            multi += 1
        if div > 0:
            div -= 1
            DFS(i + 1, int(number / num[i]))
            div += 1


N = int(input())
num = list(map(int, input().split()))
add, minus, multi, div = map(int, input().split())

max_num, min_num = - sys.maxsize, sys.maxsize
DFS(1, num[0])

print(max_num)
print(min_num)
