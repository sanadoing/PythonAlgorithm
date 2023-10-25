T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    company_a = P * W
    if R >= W:
        company_b = Q
    else:
        company_b = Q + (W - R) * S

    print(f'#{test_case} {min(company_a,company_b)}')