T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = 0
    if len(A) >= len(B):
        for i in range(len(A)-len(B)+1):
            temp = 0
            for j in range(len(B)):
                temp += A[i+j]*B[j]
            result = max(temp, result)
    else:
        for i in range(len(B)-len(A)+1):
            temp = 0
            for j in range(len(A)):
                temp += B[i+j]*A[j]
            result = max(temp, result)

    print(f'#{test_case} {result}')
