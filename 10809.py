string = input()
numbers = [-1] * 26
for i in range(len(string)):
    if numbers[ord(string[i])-97] == -1:
        numbers[ord(string[i]) - 97] = i
print(' '.join(map(str, numbers)))