t = int(input())
for _ in range(t):
    n, string = map(str, input().split())
    n = int(n)
    for s in string:
        for _ in range(n):
            print(s, end='')
    print()
