T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    result = ''
    print(f'#{test_case}')
    for _ in range(N):
        s, cnt = map(str, input().split())
        for _ in range(int(cnt)):
            result += s
    for i in range(len(result)//10+1):
        if i == len(result)//10:
            print(result[i*10:])
        else:
            print(result[i*10:(i*10)+10])
