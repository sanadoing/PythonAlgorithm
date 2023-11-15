N = int(input())
result1, result2 = 0, 0
for _ in range(N):
    t, w, h, l = map(str, input().split())
    w, h, l = int(w), int(h), int(l)
    if t == 'A':
        cnt = (w // 12) * (h // 12) * (l // 12)
        result1 += 500 * cnt + 1000
        result2 += 4000 * cnt
    else:
        result1 += 120 * 50

print(result1)
print(result2)
