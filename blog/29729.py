import sys
input=sys.stdin.readline
max_size, sn, dn = map(int, input().split())
cnt = 0
temp_size = max_size
for _ in range(sn+dn):
    command = int(input())
    if command == 1:
        cnt += 1
    else:
        cnt -= 1
    if cnt > temp_size:
        temp_size += temp_size

print(temp_size)