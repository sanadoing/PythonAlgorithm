N = int(input())
cnt = int(input())
recommend = list(map(int, input().split()))
picture = []  # 학생 넘버, 처음 추천 받은 시점, 추천 수

for i in range(cnt):

    for p in picture:
        if p[0] == recommend[i]:
            p[2] += 1
            break
    else:
        if len(picture) == N:
            picture.pop()
        picture.append([recommend[i], i, 1])

    picture.sort(key=lambda x: (-x[2], -x[1]))


picture.sort()
for p in picture:
    print(p[0], end = ' ')
