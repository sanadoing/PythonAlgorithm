numbers = list(map(int, input()))
temp, idx = 0, 0
while idx < len(numbers):
    temp += 1
    temp_str = str(temp)
    if str(numbers[idx]) in temp_str:
        for i in range(len(temp_str)):
            if str(numbers[idx]) == temp_str[i]:
                idx += 1
                if idx == len(numbers):
                    break
print(temp)
