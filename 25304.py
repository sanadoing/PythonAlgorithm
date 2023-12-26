total = int(input())
n = int(input())
total_t = 0
for _ in range(n):
    p, c= map(int, input().split())
    total_t += p*c
print("Yes" if total ==total_t else "No")