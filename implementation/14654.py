N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_score, B_score = 0, 0
max_score = 0
before, now = '', ''

for i in range(N):
    if A[i] == B[i]:  # 서로 값이 같을 경우
        if before == 'A':
            now = 'B'
            B_score += 1
            A_score = 0
        if before == 'B':
            now = 'A'
            A_score += 1
            B_score = 0

    else:  # 서로 값이 다를 경우
        if (A[i], B[i]) in ((2, 1), (1, 3), (3, 2)):
            now = 'A'  # A가 이김
            A_score += 1
            B_score = 0
        elif (A[i], B[i]) in ((1, 2), (2, 3), (3, 1)):
            now = 'B'  # B가 이김
            B_score += 1
            A_score = 0

    max_score = max(A_score, B_score, max_score)

    if now == 'A':
        before = 'A'
    elif now == 'B':
        before = 'B'

print(max_score)
