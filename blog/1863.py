N = int(input())
buildings = []
result = 0
for _ in range(N):
    x, y = map(int, input().split())
    if y == 0:
        result += len(buildings)
        buildings = []
    else:
        if len(buildings) == 0:
            buildings.append(y)
        else:
            while len(buildings) > 0 and buildings[-1] > y:
                buildings.pop()
                result += 1
            if len(buildings) > 0 and buildings[-1] == y:
                continue
            else:
                buildings.append(y)
print(len(buildings) + result)
