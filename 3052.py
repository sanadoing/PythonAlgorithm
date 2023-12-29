dic = dict()
for _ in range(10):
    n = int(input())
    if n%42 not in dic:
        dic[n%42] = 0
print(len(dic))