n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
temp_k = k

# while m > 0:
#     if temp_k == 0:
#         temp_k = k
#         result += numbers[-2]
#     else:
#         temp_k -= 1
#         result += numbers[-1]
#     m -= 1
#
# print(result)

# m이 100억 이상 커질 시, 위의 코드는 시간초과가 뜰 것.

count = int(m/(k+1)) * k
count += m % (k+1)

result += count * numbers[-1]
result += (m-count) * numbers[-2]
print(result)