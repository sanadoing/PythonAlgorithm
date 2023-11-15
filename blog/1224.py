swit_n = int(input())
switch = list(map(int, input().split()))
stu_n = int(input())

for _ in range(stu_n):
    g, n = map(int, input().split())
    if g == 1:
        temp = n
        while n < swit_n + 1:
            switch[n - 1] = (switch[n - 1] + 1) % 2
            n += temp
    else:
        l_n, r_n = n - 1, n - 1
        switch[n - 1] = (switch[n - 1] + 1) % 2
        while True:
            l_n, r_n = l_n - 1, r_n + 1
            if 0 <= l_n and r_n < swit_n and switch[l_n] == switch[r_n]:
                t = (switch[l_n] + 1) % 2
                switch[l_n], switch[r_n] = t, t
            else:
                break

for i in range(len(switch)//10+1):
    print(' '.join(map(str, switch[i*10:(i*10)+10])))
