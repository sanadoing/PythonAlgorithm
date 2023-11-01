T = int(input())

for _ in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    team = dict()
    for i in range(N):
        if team.get(score[i], 0) == 0:
            team[score[i]] = [1, i, [i]]
        else:
            c, s, p = team[score[i]]
            p.append(i)
            team[score[i]] = [c + 1, s + i, p]

    sort_team = sorted(team.items(), key=lambda item: (item[1][0], item[1][2]))
    result = 0
    fifth = []
    for s in sort_team:
        if s[1][0] < 6:
            continue
        else:




