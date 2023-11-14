import sys
input = sys.stdin.readline
N, M = map(int, input().split())
print((pow(M, N) - pow((M - 1), N)) % 1000000007)
