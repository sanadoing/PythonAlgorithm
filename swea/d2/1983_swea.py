grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    score = [0] * N

    for i in range(N):
        mid, fin, hom = map(int, input().split())
        score[i] = [mid * 0.35 + fin * 0.45 + hom * 0.2, i + 1]
    score.sort(key=lambda x: x[0], reverse=True)
    cnt = 0
    g = 0
    for i in range(N):
        if score[i][1] == K:
            print(f'#{test_case} {grade[g]}')
        cnt += 1
        if cnt == N // 10:
            cnt = 0
            g += 1
