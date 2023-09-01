# if __name__ == "__main__":
#     n = int(input())
#     dic = dict()
#     l = []
#
#     for i in range(n):
#         t, r = map(int, input().split())
#         l.append((t, r))
#
#     l.sort(key=lambda x: (x[0], -x[1]))
#
#     time_now = 1
#     result = 0
#
#
#     for i in range(n):
#         temp_t, temp_r = l[i][0], l[i][1]
#
#         if time_now <= temp_t:
#             result += temp_r
#             time_now += 1
#
#     print(result)

    # dic[t] = max(dic.get(t, r), r)

    # print(dic)
    # print(sum(dic.values()))




import sys
import heapq

n = int(input())
array = []
for _ in range(n):
    deadline, cupNoodle = map(int,sys.stdin.readline().strip().split())
    array.append((deadline, cupNoodle))

array.sort()

queue = []
print(array)
for i in array:
    print(queue)
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)

print(sum(queue))


