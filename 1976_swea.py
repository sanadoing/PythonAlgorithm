T = int(input())

for test_case in range(1, T + 1):
    h1, m1, h2, m2 = map(int, input().split())
    m_r = (m1 + m2) % 60
    h_r = ((m1 + m2) // 60 + h1 + h2) % 12
    if h_r == 0:
        h_r = 12
    print(f'#{test_case} {h_r} {m_r}')