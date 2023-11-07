import copy

N, K = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(K):

    if len(A) > 1:
        temp_A = []
        for i in range(len(A)-1):
            temp_A.append(A[i+1]-A[i])
        A = copy.deepcopy(temp_A)

print(','.join(map(str, A)))