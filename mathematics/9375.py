T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for _ in range(N):
        c_n, c_t = map(str, input().split())
        if dic.get(c_t, 0) == 0:
            dic[c_t] = 1
        else:
            dic[c_t] += 1

    result = 1
    for i in dic:
        result *= (dic[i] + 1)

    print(result -1)