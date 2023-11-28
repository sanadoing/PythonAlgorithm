n = int(input())
m = int(input())
lights = list(map(int, input().split()))
result = max((lights[0] - 0), n - lights[-1])
for i in range(len(lights)-1):
    if (lights[i+1]-lights[i]) % 2 == 1:
        result = max(result, (lights[i+1]-lights[i])//2+1)
    else:
        result = max(result, (lights[i + 1] - lights[i]) // 2)
print(result)