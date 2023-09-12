H, W = map(int, input().split())
block = list(map(int, input().split()))
result = 0

for i in range(1, len(block) - 1):
    left_max = max(block[:i])
    right_max = max(block[i + 1:])

    rain = min(left_max, right_max)

    if rain > block[i]:
        result += rain-block[i]


print(result)
