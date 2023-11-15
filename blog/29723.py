N, M, K = map(int, input().split())
dic = dict()
result1, result2 = 0, 0

for i in range(N):
    subj, score = map(str, input().split())
    dic[subj] = int(score)

for i in range(K):
    dele = input()
    result1 += dic[dele]
    result2 += dic[dele]
    dic.pop(dele)

dic_sort = sorted(dic.items(), key=lambda item: item[1])
for i in range(M - K):
    result1 += dic_sort[i][1]
    result2 += dic_sort[len(dic_sort) - i - 1][1]

print(result1, result2)
