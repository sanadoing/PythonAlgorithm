# small = []
#
# for _ in range(9):
#     small.append(int(input()))
#
# print(small)
# # small.remove(7)
# small.remove(small[8])
# print(small)
# # print(small.remove(small[]))
#
# # for i in range(9):
# #     sum_weight = sum(small)
# #     sum_weight -= small[i]
# #
# #     for j in range(9):
# #         if i != j:
# #             sum_weight -= small[j]
# #
# #             if sum_weight == 100:
# #                 small[i] = 0
# #                 small[j] = 0
# #                 small.sort()
# #                 print('\n'.join(map(str, small[2:])))
# #                 exit(0)
# #             sum_weight += small[j]
# #
# #     sum_weight += small[i]
# #
# #


import sys

input = sys.stdin.readline

arr = []
d = []
for _ in range(9):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            # tmp1 = arr[i]
            # tmp2 = arr[j]
            print(arr)
            print(i, j, arr[i])
            arr.remove(arr[i])
            print(arr)
            print(i, j, arr[j])
            arr.remove(arr[j])
            print(arr)
            arr.sort()
            for i in arr:
                print(i)
            exit(0)

# arr.remove(tmp1)
# arr.remove(tmp2)


