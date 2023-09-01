# https://www.acmicpc.net/problem/17178
# 접근방법
# 주어진 줄에 있는 모든 사람을 한줄로 세워서 오름차순으로 정렬한다.
# 현재 줄 앞에 있는 사람을 모두 탐색하며 오름차순으로 정렬한 줄의 현재 탐색 중인 인덱스의 값과 동일한 좌석이 있다면 반복해서 빼내어 준다.
# 이후 줄을 하나씩 탐색하며 가장 앞에 있는 사람 중 번호가 가장 늦은 사람을 앞으로 보낸다.
# 모든 줄을 탐색한 뒤, 남아있는 사람이 있는지 확인하여 있다면 Bad, 없다면 Good을 출력한다.
#
# from collections import deque
#
# n = int(input())
# array = [deque(input().split()) for _ in range(n)]
# a = []
# for x in array:
#     for x_ in x:
#         a.append(x_)
# a.sort()
#
# stack = []
# i = 0
# for _ in range(n*5):
#     while True:
#         check = True
#         for j in range(n):
#             if array[j] and a[i] == array[j][0]:
#                 array[j].popleft()
#                 i += 1
#                 check = False
#                 break
#         if stack and a[i] == stack[-1]:
#             stack.pop()
#
#             i += 1
#             check = False
#         if check:
#             break
#
#     max_v = ''
#     idx = 0
#     for j in range(n):
#         if array[j] and max_v < array[j][0]:
#             idx = j
#             max_v = array[j][0]
#     if max_v:
#         array[idx].popleft()
#         stack.append(max_v)
#
# print(array)
# print(stack)


import sys
import heapq as hq

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
arr = []

a.sort(reverse=True)
# 8 4 4 1 1
for i in a:
    if len(arr) < m:
        hq.heappush(arr, i)
    else:
        hq.heappush(arr, hq.heappop(arr) + i)

print(max(arr))
