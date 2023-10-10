N = int(input())
result = 0

for i in range(1, N+1):
    now = list(str(i))
    if len(now) == 1 or len(now) == 2:
        result += 1
        continue

    first = True
    temp = 0
    for j in range(len(now)-1):
        if first:
            temp = int(now[j]) - int(now[j+1])
            first = False
        else:
            if temp == int(now[j]) - int(now[j+1]):
                continue
            else:
                break
    else:
        result += 1

print(result)



