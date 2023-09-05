H, W = map(int, input().split())
block = list(map(int, input().split()))

temp = block[0]
result = 0

for i in range(1, W):
    if temp > block[i]:
        result += temp - block[i]
    else:
        temp = block[i]



print(result)
