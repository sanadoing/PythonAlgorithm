import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = dict()
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
result = sorted(dic.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
for i in range(len(result)):
    print(result[i][0])