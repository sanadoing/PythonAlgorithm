N = int(input())
word = list(input())
result = 0

for _ in range(N - 1):
    word_temp = word[:]
    target = input()
    cnt = 0
    for t in target:
        if t in word_temp:
            word_temp.remove(t)
        else:
            cnt += 1

    if cnt < 2 and len(word_temp) < 2:
        result += 1

print(result)
