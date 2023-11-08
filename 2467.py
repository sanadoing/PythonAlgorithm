N = int(input())
numbers = list(map(int, input().split()))
left, right = 0, N - 1
t = int(1e9)*2 + 1
result1, result2 = 0, 0
while left < right:
    hap = numbers[left]+numbers[right]
    if abs(hap) <= t:
        result1, result2 = numbers[left], numbers[right]
        t = abs(hap)
    if hap < 0:
        left += 1
    else:
        right -= 1
print(result1, result2)
