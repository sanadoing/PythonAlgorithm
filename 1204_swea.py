T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    students = list(map(int, input().split()))
    dic = dict()
    fre_max = -1

    for s in students:
        if dic.get(s, 0) == 0:
            dic[s] = 1
        else:
            dic[s] += 1

        fre_max = max(fre_max, dic[s])
    result = -1
    for n in dic.keys():
        if fre_max == dic[n]:
            result = max(result, n)

    print(f'#{test_case} {result}')
