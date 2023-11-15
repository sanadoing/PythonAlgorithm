N = int(input())
string = map(str, input())
BS = list('BRONZESILVER')
dic = dict()
for s in string:
    if s in BS:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
if len(dic) < 10:
    print(0)
else:
    dic['R'] //= 2
    dic['E'] //= 2
    sdic = sorted(dic.items(), key=lambda item: item[1])
    print(sdic[0][1])

