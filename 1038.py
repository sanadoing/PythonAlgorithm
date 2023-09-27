from itertools import combinations

N = int(input())
des_num = []

for i in range(1, 11):
    for con in combinations(range(0, 10), i):
        con_list = list(con)
        con_list.sort(reverse=True)
        des_num.append(int(''.join(map(str, con_list))))


des_num.sort()

try:
    print(des_num[N])
except:
    print(-1)

# if N > len(des_num):
#     print(-1)
# else:
#     print(des_num[N])