N, M = map(int, input().split())
player = []
player_score = [0] * N
for i in range(N):
    player.append(sorted(list(map(int, input().split())), reverse=True))

for i in range(M):

    max_score = 0
    for j in range(N):
        max_score = max(max_score, player[j][i])

    for j in range(N):
        if player[j][i] == max_score:
            player_score[j] += 1

for i in range(N):
    if max(player_score) == player_score[i]:
        print(i + 1, end=' ')
