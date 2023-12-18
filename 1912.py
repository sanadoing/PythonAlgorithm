n = int(input())
numbers = list(map(int, input().split()))
result = -1001
for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])
print(max(numbers))
