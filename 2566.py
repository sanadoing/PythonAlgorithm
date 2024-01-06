result = [0, 0, -1]
for i in range(9):
    temp = list(map(int, input().split()))
    for j in range(9):
        if result[2] < temp[j]:
            result = [i+1, j+1, temp[j]]

print(result[2])
print(result[0], result[1])
