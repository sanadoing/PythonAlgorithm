import sys
input = sys.stdin.readline

N, S = map(int, input().split())
number = list(map(int, input().split()))
s, e = 0, 1
sum_number = number[s]
result = sys.maxsize

while True:

    if e == N and sum_number < S:
        break

    if sum_number >= S:
        result = min(result, e - s)
        sum_number -= number[s]
        s += 1
    else:
        sum_number += number[e]
        e += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)
