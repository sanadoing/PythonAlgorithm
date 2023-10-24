N = int(input())
arr = list(map(int, input().split()))

arrset = list(set(arr))
arrset.sort()
dic = dict()

for i in range(len(arrset)):
    dic[arrset[i]] = i

for i in range(len(arr)):
    print(dic[arr[i]], end=' ')