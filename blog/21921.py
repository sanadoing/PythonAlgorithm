N, X = map(int, input().split())
numbers = list(map(int, input().split()))
maxN, cnt = sum(numbers[0:X]), 1
sumN = maxN
for i in range(1, len(numbers)-X+1):
    sumN = sumN - numbers[i-1] + numbers[i+X-1]
    if sumN > maxN:
        maxN = sumN
        cnt = 1
    elif sumN == maxN:
        cnt += 1
if maxN == 0:
    print("SAD")
else:
    print(maxN)
    print(cnt)



