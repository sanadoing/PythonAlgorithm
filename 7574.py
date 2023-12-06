from collections import deque,defaultdict

n, r = map(int, input().split())
leaves = defaultdict(list)
check = [0] * (n)

for i in range(n):
    x, y = map(int, input().split())
    leaves[(x, y)] = [(x + r, y + r), i]

d = int(input())
queue = deque([])
queue.append(leaves[0])
result = -1
check[0] = 1
temp_leaves = leaves[1:]
while queue:
    min_node, max_node, idx = queue.popleft()
    min_node_x, min_node_y = min_node
    max_node_x, max_node_y = max_node
    check[idx] = 1
    result = max(result, max_node_x + max_node_y)
    for i in range(n):
        leaf = leaves[i]
        if check[i] == 0:
            leaf_min_node, leaf_max_node = leaf[0], leaf[1]
            if (0 <= min_node_x - leaf_max_node[0] <= d) and (
                    min_node_y <= leaf_max_node[1] <= max_node_y or leaf_min_node[1] <= max_node_y <= leaf_max_node[1]):
                queue.append(leaves[i])
            elif (0 <= min_node_y - leaf_max_node[1] <= d) and (
                    min_node_x <= leaf_max_node[0] <= max_node_x or leaf_min_node[0] <= max_node_x <= leaf_max_node[0]):
                queue.append(leaves[i])
            elif (0 <= leaf_min_node[0] - max_node_x <= d) and (
                    min_node_y <= leaf_min_node[1] <= max_node_y or leaf_min_node[1] <= min_node_y <= leaf_max_node[1]):
                queue.append(leaves[i])
            elif (0 <= leaf_min_node[1] - max_node_y <= d) and (
                    min_node_x <= leaf_min_node[0] <= max_node_x or leaf_min_node[0] <= min_node_x <= leaf_max_node[0]):
                queue.append(leaves[i])

print(result)
