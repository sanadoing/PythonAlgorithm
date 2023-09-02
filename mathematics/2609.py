a, b = map(int, input().split())
max_num = max(a, b)
min_num = min(a, b)

for i in range(min_num, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

idx = 1

while True:
    if (max_num * idx) % min_num == 0:
        print((max_num * idx))
        break
    idx += 1
