J, N = map(int, input().split())
result = 0
for _ in range(N):
    string = list(map(str, input()))
    size = 0
    for s in string:
        if s == ' ':
            size += 1
        else:
            if ord(s) < 58 or 96 < ord(s):
                size += 2
            else:
                size += 4
        if size > J:
            break
    else:
        result += 1
print(result)
