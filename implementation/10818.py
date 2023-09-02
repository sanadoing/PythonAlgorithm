import sys

N = int(input())
num = list(map(int, input().split()))

min_num = sys.maxsize
max_num = -sys.maxsize

for i in range(N):
    if num[i] < min_num:
        min_num = num[i]
    if num[i] > max_num:
        max_num = num[i]

print(min_num,max_num)

