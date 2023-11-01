string = input()
dic = dict()
string = string.upper()
for s in string:
    if dic.get(s, 0) == 0:
        dic[s] = 1
    else:
        dic[s] += 1

sort_list = sorted(dic.items(), key=lambda item: item[1])

if len(sort_list) >= 2 and sort_list[-1][1] == sort_list[-2][1]:
    print("?")

else:
    print(sort_list[-1][0])
