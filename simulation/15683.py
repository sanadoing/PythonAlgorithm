dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv = []  # {cctv_num : (y, x), (y, x)}
# cctv1 = [[0], [1], [2], [3]]
# cctv2 = [[0, 2], [1, 3]]
# cctv3 = [[0, 1], [1, 2], [2, 3], [3, 0]]
# cctv4 = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 1, 2]]
# cctv5 = [[0, 1, 2, 3]]
five_cctv = [[[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 1, 2]], [[0, 1, 2, 3]]]

for y in range(N):
    for x in range(M):
        if room[y][x] != 0 and room[y][x] != 6:
            cctv.append([room[y][x], y, x])

print(cctv)


def DFS(cnt, cctv_dlist):
    temp = cctv_dlist
    if cnt == len(cctv):
        print(cctv_dlist)
        for c in cctv_dlist:
            cctv_num, cctv_y, cctv_x, cctv_d = c[0], c[1], c[2], c[3]

        return
    else:
        for i in range(len(five_cctv[cnt])):
            p, y, x = cctv[cnt]
            temp.append([p, y, x, i])
            DFS(cnt + 1, temp)
            temp.pop()


DFS(0, [])
