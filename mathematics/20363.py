x, y = map(int, input().split())

print((x + y // 10 + y) if x >= y else (y + x // 10 + x))
