t = int(input())
for _ in range(t):
    n = int(input())
    result = [0, 0, 0, 0]
    if n >= 25:
        result[0] = (n // 25)
        n = n-(n // 25)*25
    if n >= 10:
        result[1] = (n // 10)
        n = n-(n // 10)*10
    if n >= 5:
        result[2] = (n // 5)
        n = n-(n // 5)*5
    result[3] = n
    print(' '.join(map(str, result)))
