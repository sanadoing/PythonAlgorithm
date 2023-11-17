from collections import deque
for _ in range(10):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = deque(numbers)
    n = 1
    while True:
        now = numbers.popleft()-n
        if now <= 0:
            now = 0
            numbers.append(now)
            break
        numbers.append(now)
        n += 1
        if n == 6:
            n = 1
    print(f'#{N}', end=' ')
    print(' '.join(map(str, numbers)))
