
def comb(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result

N = 3
arr = [1, 2, 3]

sel = [0] * N
check = [0] * N
result = []

def perm(idx):
    global result
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0


perm(0)



import itertools

arr1 = [1, 2, 3, 4]

for i in itertools.permutations(arr1, 4):
    print(list(i), end=' ')

for i in itertools.combinations(arr1, 3):
    print(list(i), end=' ')

