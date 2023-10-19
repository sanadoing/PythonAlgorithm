import copy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv = []  # [cctv_num, y, x]
# cctv1 = [[0], [1], [2], [3]]
# cctv2 = [[0, 2], [1, 3]]
# cctv3 = [[0, 1], [1, 2], [2, 3], [3, 0]]
# cctv4 = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
# cctv5 = [[0, 1, 2, 3]]
five_cctv = [[[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
zero_cnt = 0
result = 0
for y in range(N):
    for x in range(M):
        if room[y][x] != 0 and room[y][x] != 6:
            cctv.append([room[y][x], y, x])
        if room[y][x] == 0:
            zero_cnt += 1


def DFS(cnt, cctv_dlist):
    global room, result
    temp = cctv_dlist

    if cnt == len(cctv):
        temp_result = 0
        room_copy = copy.deepcopy(room)

        for c in cctv_dlist:
            cctv_num, cctv_y, cctv_x, cctv_d = c[0], c[1], c[2], c[3]

            for i in range(len(five_cctv[cctv_num - 1][cctv_d])):
                d = five_cctv[cctv_num - 1][cctv_d][i]
                yy = cctv_y + dy[d]
                xx = cctv_x + dx[d]
                while True:
                    if 0 <= yy < N and 0 <= xx < M:
                        if room_copy[yy][xx] == 0:
                            room_copy[yy][xx] = '#'
                            temp_result += 1
                        elif room_copy[yy][xx] == 6:
                            break

                    else:
                        break

                    yy += dy[d]
                    xx += dx[d]

        result = max(result, temp_result)
        return
    else:
        for i in range(len(five_cctv[cctv[cnt][0] - 1])):
            p, y, x = cctv[cnt]
            temp.append([p, y, x, i])
            DFS(cnt + 1, temp)
            temp.pop()


DFS(0, [])
print(zero_cnt - result)
