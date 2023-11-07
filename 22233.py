import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = dict()
result = N
keywords = list(input().strip() for _ in range(N))
keywords = set(keywords)

for _ in range(M):
    blog = list(map(str, input().strip().split(',')))
    blog = set(blog)
    keywords -= blog
    print(len(keywords))
