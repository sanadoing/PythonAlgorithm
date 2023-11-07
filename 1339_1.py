import math

N = int(input())
dic = dict()
result = 0
for _ in range(N):
    word = list(map(str, input()))
    for i in range(len(word)):
        if dic.get(word[i], 0) == 0:
            dic[word[i]] = int(math.pow(10, len(word) - i))
        else:
            dic[word[i]] += int(math.pow(10, len(word) - i))

temp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
cost = 9

for i in range(len(temp)):
    result += (temp[i][1] * cost) // 10
    cost -= 1

print(result)
