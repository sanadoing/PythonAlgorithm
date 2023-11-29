import sys
N = int(sys.stdin.readline().strip())

while True:
    button = True
    for i in str(N):
        if i != '4' and i != '7':
            button = False
            N -= 1
    if button:
        print(N)
        break