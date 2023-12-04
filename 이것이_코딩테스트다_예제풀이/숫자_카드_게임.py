# n, m = map(int, input().split())
# numbers = []
# result = -1
# for _ in range(n):
#     l = list(map(int, input().split()))
#     numbers.append(l)
#     temp = min(l)
#     if temp > result:
#         result = temp
# print(result)
#

# 변수 명을 포함하여 코드 디벨롭
n, m = map(int, input().split())
result = 0
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(min_value, result)
print(result)
