n, k = map(int, input().split())
result = 0
# while n != 1:
#     if n % k == 0:
#         n //= k
#     else:
#         n -= 1
#     result += 1
# print(result)

while True:
    target = (n // k) * k
    result += (n - target)  #   n이 k로 나눠지는 수가 될 때까지 1을 한번에 빼줌
    n = target  #   1을 한번에 뺐으므로, target(k로 나눠지는 수) 은 n이 됨.
    if n < k:   #   더 이상 k로 나눌 수 없는 경우
        break
    result += 1
    n //= k     #   n을 k로 나눠줌

result += (n-1)
print(result)
