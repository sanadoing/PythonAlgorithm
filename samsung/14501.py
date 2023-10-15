day = int(input())
schedule = [list(map(int, input().split())) for _ in range(day)]
dp = [0 for i in range(day+1)]
print(schedule)

for i in range(day):
    print(i, 'time',schedule[i][0], 'money', schedule[i][1])
    for j in range(i+schedule[i][0], day+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
        print(dp)

print(dp[-1])
