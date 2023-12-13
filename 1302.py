from collections import defaultdict

n = int(input())
dic = defaultdict(list)
for _ in range(n):
    book = input()
    if book not in dic:
        dic[book] = 1
    else:
        dic[book] += 1

sort_books = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(sort_books[0][0])
