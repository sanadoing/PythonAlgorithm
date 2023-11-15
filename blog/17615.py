N = int(input())
balls = list(map(str, input()))
result1, result2 = 0, 0
fb = balls[-1]
flag = False
for i in range(len(balls) - 2, -1, -1):
    if balls[i] == fb and flag:
        result1 += 1
    elif balls[i] != fb:
        flag = True
        result2 += 1
print(min(result1, result2))
