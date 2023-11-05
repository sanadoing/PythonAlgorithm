N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort(key=lambda x: (-x[1], -x[2], -x[3]))
grade = 1
temp_grade = 0
for i in range(len(medals)):
    # 앞에 값과 메달 현황이 다를 경우
    if i > 0 and (
            medals[i - 1][1] != medals[i][1] or medals[i - 1][2] != medals[i][2] or medals[i - 1][3] != medals[i][3]):
        grade += temp_grade
        temp_grade = 1
    else:
        temp_grade += 1

    if medals[i][0] == K:
        print(grade)
