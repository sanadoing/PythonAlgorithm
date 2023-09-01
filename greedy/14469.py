import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    cow = []

    for _ in range(N):
        a, b = map(int, input().split())
        cow.append((a, b))

    cow.sort()
    now = 1

    for i in range(N):
        if now <= cow[i][0]:
            now = cow[i][0] + cow[i][1]
        else:
            now = now + cow[i][1]

    print(now)