y, m, d = map(int, input().split('-'))
N = int(input())
dd = (d + N) % 30
if dd == 0:
    dd = 30
    mm = (m + (d + N) // 30 - 1) % 12
else:
    mm = (m + (d + N) // 30) % 12
if mm == 0:
    mm = 12
    yy = y + (m + (d + N) // 30) // 12 - 1
else:
    yy = y + (m + (d + N) // 30) // 12
if mm < 10:
    mm = str('0') + str(mm)
if dd < 10:
    dd = str('0') + str(dd)
print(f"{yy}-{mm}-{dd}")
