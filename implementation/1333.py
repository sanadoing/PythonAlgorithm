N, L, D = map(int, input().split())
now = 0
call = D
while True:
    now += L
    if now == call:
        print(now)
    
