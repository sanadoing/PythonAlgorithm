S = int(input())
temp = 1
temp_sum = temp
result = 1

while True:
    if S-temp <= temp_sum:
        print(result)
        break
    else:
        temp += 1
        temp_sum += temp
        result += 1

