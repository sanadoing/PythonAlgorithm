H, M = map(int, input().split())

if M < 45:
    H -= 1
    M = 60 - (45 - M)

else:
    M -= 45

if H < 0:
    H = 23
print(H, M)
