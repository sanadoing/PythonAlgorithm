N = int(input())
result, multi, total = 1, 1, 1
while True:
    if N <= total:
        break
    else:
        total += 6 * (multi)
        multi += 1
        result += 1
print(result)
