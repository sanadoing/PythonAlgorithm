arr = input()
temp = 0
flag = False
result = 0


def calculate():
    global flag, result
    if flag:
        result -= temp
    else:
        result += temp


for i in range(len(arr)):

    if arr[i] == '-':

        calculate()

        temp = 0
        flag = True
    elif arr[i] == '+':

        calculate()
        temp = 0
    else:
        temp = int(temp) * 10 + int(arr[i])

calculate()
print(result)
