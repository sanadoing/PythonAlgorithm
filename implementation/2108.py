import sys
input = sys.stdin.readline
N = int(input())
num = list(int(input()) for _ in range(N))

print(round(sum(num)/N))
num.sort()
print(num[N//2])

dic = dict()

for n in num:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

max_num = max(dic.values())

max_dic = []
for d in dic:
    if dic[d] == max_num:
        max_dic.append(d)

if len(max_dic) > 1:
    max_dic.sort()
    print(max_dic[1])
else:
    print(max_dic[0])
print(num[-1] - num[0])