N = int(input())
test_room = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
for t in test_room:
    t -= B

    if t > 0:
        if t % C > 0:
            result += (t // C) + 1
        else:
            result += (t // C)

print(result)
