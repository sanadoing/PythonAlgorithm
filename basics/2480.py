dice = list(map(int, input().split()))
max_cnt = 1
result = 0
max_cnt_n = 0
for i in range(1, 7):

    if max_cnt < dice.count(i):
        max_cnt = dice.count(i)
        max_cnt_n = i
if max_cnt == 1:
    result = max(dice) * 100
elif max_cnt == 2:
    result = 1000 + max_cnt_n * 100
else:
    result = 10000 + max_cnt_n * 1000
print(result)
