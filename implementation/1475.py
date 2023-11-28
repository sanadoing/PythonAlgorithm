N = input()
numbers = [0] * 10
for i in N:
    if int(i) == 6 or int(i) == 9:
        if numbers[6] < numbers[9]:
            numbers[6] += 1
        else:
            numbers[9] += 1
    else:
        numbers[int(i)] += 1
print(max(numbers))
