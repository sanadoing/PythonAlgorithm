a, b = map(int, input().split())
a, b = max(a, b), min(a, b)
if a == b:
    print(0)
else:
    print(a - b - 1)
    for i in range(b + 1, a):
        print(i, end=' ')
