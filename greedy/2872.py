import sys
input = sys.stdin.readline

N = int(input())

book = list(int(input()) for _ in range(N))

result = 0
check_num = len(book)
for i in range(len(book) - 1, -1, -1):
    if book[i] == check_num:
        check_num -= 1
    else:
        result += 1

print(result)
