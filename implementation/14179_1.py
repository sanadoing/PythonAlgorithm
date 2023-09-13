H, W = map(int, input().split())
block = list(map(int, input().split()))
result = 0

for i in range(1, len(block) - 1):
    left_max = max(block[:i])
    right_max = max(block[i + 1:])

    if block[i] < min(left_max, right_max):
        result += min(left_max, right_max) - block[i]


print(result)

