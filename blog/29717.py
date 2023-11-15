import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    left, right = 1, 1e9

    n = int(input().rstrip())
    exp = n * (n + 1) // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) <= exp:
            left = mid + 1
        else:
            right = mid - 1
    print(int(left))