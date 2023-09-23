N = int(input())
crain = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
result = 0
crain.sort(reverse=True)
box.sort(reverse=True)


if crain[0] < box[0]:
    print(-1)
else:

    while len(box) > 0:
        for c in crain:
            if box and c < box[-1]:
                continue
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        result += 1

    print(result)

