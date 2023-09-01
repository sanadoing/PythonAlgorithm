N = int(input())
men = list(map(int, input().split()))
women = list(map(int, input().split()))

visited_w = [0] * N

men.sort()
women.sort()

m_p = 0
w_p = N - 1

result = 0

while m_p < N and 0 <= w_p:

    if men[m_p] < 0 and 0 < women[w_p] and abs(men[m_p]) > abs(women[w_p]):
        result += 1
        m_p += 1
        w_p -= 1
    elif 0 < men[m_p] and women[w_p] < 0 and abs(men[m_p]) < abs(women[w_p]):
        result += 1
        m_p += 1
        w_p -= 1
    elif men[m_p] < 0 and 0 < women[w_p] and abs(men[m_p]) <= women[w_p]:
        w_p -= 1
    elif 0 < men[m_p]  and women[w_p] < 0 and men[m_p] >= abs(women[w_p]):
        w_p -= 1
    elif men[m_p] < 0 and women[w_p] < 0:
        m_p += 1
    elif 0 < men[m_p] and 0 < women[w_p]:
        w_p -= 1



print(result)
