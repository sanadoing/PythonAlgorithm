t = int(input())

for _ in range(t):
    word = input()
    n = int(input())
    memo = [[] for _ in range(27)]
    result = []
    for i in range(len(word)):
        alpha = ord(word[i]) - ord('a')
        memo[alpha].append(i)
        if len(memo[alpha]) >= n:
            result.append(word[memo[alpha][-n]:memo[alpha][-1] + 1])

    if len(result) == 0:
        print(-1)
    else:
        result.sort(key=lambda x: len(x))
        print(len(result[0]), len(result[-1]))
