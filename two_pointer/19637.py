import sys
input = sys.stdin.readline
N, M = map(int, input().split())
grade = [list(map(str, input().split())) for _ in range(N)]
for _ in range(M):
    power = int(input())
    left, right = 0, len(grade) - 1
    while left < right:
        mid = (left + right) // 2
        if int(grade[mid][1]) < power:
            left = mid + 1
        else:
            right = mid
    print(grade[right][0])
