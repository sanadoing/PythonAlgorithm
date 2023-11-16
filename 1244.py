T = int(input())

def DFS(c):
    global numbers, result
    if c == 0:
        result = max(int(''.join(numbers)), result)
        return
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            temp = ''.join(numbers)
            if check.get((temp, c-1), 1):
                check[(temp, c-1)] = 0
                print(temp, check)
                DFS(c-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


for test_case in range(1, T + 1):
    numbers, cnt = input().split()
    numbers = list(numbers)
    cnt = int(cnt)
    check = {}
    result = -1
    DFS(cnt)
    print(f"#{test_case} {result}")
