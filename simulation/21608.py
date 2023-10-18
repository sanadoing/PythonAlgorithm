dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

N = int(input())
class_room = [[0] * N for _ in range(N)]
student = [[] for _ in range(N * N + 1)]

for _ in range(N * N):
    s, l1, l2, l3, l4 = map(int, input().split())
    student[s] = [l1, l2, l3, l4]
    temp_info = []

    for y in range(N):
        for x in range(N):

            if class_room[y][x] == 0:
                l_c, z_c = 0, 0
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < N and 0 <= xx < N:
                        if class_room[yy][xx] in student[s]:
                            l_c += 1
                        if class_room[yy][xx] == 0:
                            z_c += 1

                temp_info.append([l_c, z_c, y, x])

    temp_info.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    class_room[temp_info[0][2]][temp_info[0][3]] = s

result = 0
for y in range(N):
    for x in range(N):
        like_cnt = 0
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]

            if 0 <= yy < N and 0 <= xx < N and class_room[yy][xx] in student[class_room[y][x]]:
                like_cnt += 1

        if like_cnt == 1:
            result += 1
        elif like_cnt == 2:
            result += 10
        elif like_cnt == 3:
            result += 100
        elif like_cnt == 4:
            result += 1000

print(result)
