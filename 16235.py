from collections import deque

ddy = [-1, -1, -1, 0, 1, 1, 1, 0]
ddx = [-1, 0, 1, 1, 1, 0, -1, -1]
n, m, k = map(int, input().split())
ground = [[5] * n for _ in range(n)]
nourishment = [list(map(int, input().split())) for _ in range(n)]
trees_point = deque([])
trees = [[[]] * n for _ in range(n)]
dead_trees = deque([])
parents_trees = deque([])
for _ in range(m):
    x, y, age = map(int, input().split())
    if [x, y] not in trees_point:
        trees_point.append([x, y])
    if len(trees[y][x]) > 0:
        trees[y][x].append(age)
    else:
        trees[y][x] = [age]


def spring():
    global trees_point, ground, trees
    temp_trees_point = deque([])
    while trees_point:
        tpx, tpy = trees_point.popleft()
        trees[tpy][tpx].sort()
        temp_trees = []
        for i in range(len(trees[tpy][tpx])):
            if trees[tpy][tpx][i] <= ground[tpy][tpx]:
                ground[tpy][tpx] -= trees[tpy][tpx][i]
                temp_trees.append(trees[tpy][tpx][i] + 1)
                if (trees[tpy][tpx][i] + 1) % 5 == 0:
                    parents_trees.append([tpx, tpy])
            else:
                dead_trees.append([tpx, tpy, trees[tpy][tpx][i]])
        trees[tpy][tpx] = temp_trees
        if len(temp_trees) > 0:
            temp_trees_point.append([tpx, tpy])
    trees_point = temp_trees_point


def summer():
    global dead_trees
    while dead_trees:
        dx, dy, da = dead_trees.popleft()
        ground[dy][dx] += (da // 2)


def fall():
    global parents_trees, trees, trees_point
    visited = [[False] * n for _ in range(n)]
    while parents_trees:
        px, py = parents_trees.popleft()
        visited[py][px] = True
        for i in range(8):
            yy, xx = ddy[i] + py, ddx[i] + px
            if 0 <= yy < n and 0 <= xx < n and visited[yy][xx] == False:
                visited[yy][xx] = True
                if [xx, yy] not in trees_point:
                    trees_point.append([xx, yy])
                if len(trees[yy][xx]) > 0:
                    trees[yy][xx].append(1)
                else:
                    trees[yy][xx] = [1]


def winter():
    for y in range(n):
        for x in range(n):
            ground[y][x] += nourishment[y][x]


while k:
    print("----------------")
    print("trees")
    for t in trees:
        print(t)
    print("trees_point")
    print(trees_point)
    print("ground")
    for t in ground:
        print(t)
    spring()
    print("after spring----------------")
    print("trees")
    for t in trees:
        print(t)
    print("trees_point")
    print(trees_point)
    print("ground")
    for t in ground:
        print(t)
    summer()
    print("after summer----------------")
    print("trees")
    for t in trees:
        print(t)
    print("trees_point")
    print(trees_point)
    print("ground")
    for t in ground:
        print(t)
    fall()
    print("after fall----------------")
    print("trees")
    for t in trees:
        print(t)
    print("trees_point")
    print(trees_point)
    print("ground")
    for t in ground:
        print(t)
    winter()
    print("after winter----------------")
    print("trees")
    for t in trees:
        print(t)
    print("trees_point")
    print(trees_point)
    print("ground")
    for t in ground:
        print(t)
    k -= 1

result = 0
for tx, ty in trees_point:
    result += len(trees[ty][tx])
print(result)
