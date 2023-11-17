N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
for i in range(len(numbers)):
    new_numbers = numbers[:i] + numbers[i + 1:]
    left = 0
    right = len(new_numbers) - 1
    while left < right:
        temp = new_numbers[left] + new_numbers[right]
        if temp == numbers[i]:
            result += 1
            break
        elif temp < numbers[i]:
            left += 1
        else:
            right -= 1
print(result)
