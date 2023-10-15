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


def comb3(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    if n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb3(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result


def comb4(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    if n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb4(arr[i+1:], n-1):
                result.append([arr[i]] + j)
    return result


arr = [1, 2, 3, 4]
print(comb4(arr, 1))

N = 3
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
arr = [(1,1), (2, 1), (3,1), (5,1)]

def comb5(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    if n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb5(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result



print(comb5(arr, 3))

for c in comb5(arr, 3):
    print(c)