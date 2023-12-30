n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
result = 0
for n in numbers:
    if n == v:
        result += 1
print(result)