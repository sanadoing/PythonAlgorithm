N = int(input())
result = 0
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:x[0])
print(arr)