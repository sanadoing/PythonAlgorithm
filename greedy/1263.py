# import sys
# input = sys.stdin.readline
#
# N = int(input())
# work = []
#
# for _ in range(N):
#     t, s = map(int, input().split())
#     work.append((t, s))
#
# work.sort(key=lambda x: (x[1], x[0]))
#
# start = work[0][1] - work[0][0]
#
# current = start
#
# while True:
#     for i in range(N):
#         if current + work[i][0] > work[i][1]:
#             start -= 1
#             break
#         else:
#             current += work[i][0]
#     else:
#         print(start)
#         break

import sys

input = sys.stdin.readline

N = int(input())
work = []

for _ in range(N):
    t, s = map(int, input().split())
    work.append((t, s))

work.sort(key=lambda x: (x[1], x[0]), reverse=True)

time = work[0][1]
for i in range(1, N):
    if time < work[i][1]:
        time -= work[i][0]
    else:
        time = work[i][1] - work[i][0]

if time < 0:
    print(-1)
else:
    print(time)