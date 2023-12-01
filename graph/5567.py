from collections import defaultdict

n = int(input())
m = int(input())
friends = defaultdict(list)
result = []


def dfs(s, depth):
    global result
    if s != 1 and s not in result:
        result.append(s)
    for v in friends[s]:
        if depth + 1 <= 2:
            dfs(v, depth + 1)


for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

dfs(1, 0)
print(len(result))
