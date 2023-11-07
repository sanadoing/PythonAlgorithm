T = int(input())

for _ in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    count = {}
    for i in range(N):
        if score[i] not in count:
            count[score[i]] = 1
        else:
            count[score[i]] += 1
    del_team = []
    for c in count.items():
        if c[1] < 6:
            del_team.append(c[0])
    dic = dict()
    rank = 1
    for i in range(N):
        if score[i] not in del_team:
            if score[i] not in dic:
                dic[score[i]] = [1, rank, 0]
            else:
                if dic[score[i]][0] < 4:
                    dic[score[i]][0] += 1
                    dic[score[i]][1] += rank
                elif dic[score[i]][0] == 4:
                    dic[score[i]][0] += 1
                    dic[score[i]][2] = rank
            rank += 1

    result = sorted(dic.items(), key=lambda x: (x[1][1], x[1][2]))
    print(result[0][0])
