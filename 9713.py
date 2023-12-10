N = int(input())

for i in range(N):
    number = int(input())
    result = 0
    for j in range(1, number + 1, 2):
        result += j
    print(result)
