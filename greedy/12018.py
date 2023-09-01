if __name__ == "__main__":
    n, m = map(int, input().split())
    c = []

    for _ in range(n):
        student, full = map(int, input().split())
        s_m = list(map(int, input().split()))
        s_m.sort()
        if student - full < 0:
            c.append(1)
        else:
            c.append(s_m[student - full])

    c.sort()
    count = 0

    for i in range(len(c)):

        if m >= c[i]:
            m -= c[i]
            count += 1

    print(count)
