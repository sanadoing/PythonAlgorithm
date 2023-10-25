N = int(input())
number = []
for _ in range(N):
    a = list(map(str, input()))
    flag = False
    temp_number = 0
    for i in range(len(a)):
        if a[i].isdigit() == True:
            flag = True
            temp_number = temp_number*10 + int(a[i])
        else:
            if flag:
                number.append(temp_number)
                temp_number = 0
            flag = False
    if flag:
        number.append(temp_number)

number.sort()
print('\n'.join(map(str, number)))