T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    dic = dict()
    cnt = 1

    while len(dic) < 10:
        result = str(N * cnt)

        for s in result:
            if dic.get(s, 0) == 0:
                dic[s] = 0
        cnt += 1

    print(f'#{test_case} {result}')
