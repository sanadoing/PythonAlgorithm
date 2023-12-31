nn, x = map(int, input().split())
numbers = list(map(int, input().split()))
for n in numbers:
    if n < x:
        print(n, end=' ')