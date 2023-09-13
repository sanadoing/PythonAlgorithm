# def recursion(cnt):
#     global result
#
#     if cnt == 0:
#         temp = 0
#         for i in range(N):
#             for j in range(4, len(word[i]) - 4):
#                 if alphabet.get(word[i][j], 0) == 0:
#                     break
#             else:
#                 temp += 1
#         result = max(result, temp)
#         return
#
#     for i in range(N):
#         for j in range(4, len(word[i]) - 4):
#             if alphabet.get(word[i][j], 0) == 0:
#                 alphabet[word[i][j]] = 1
#                 recursion(cnt - 1)
#                 alphabet[word[i][j]] = 0
#
#
# N, K = map(int, input().split())
# word = [list(map(str, input())) for _ in range(N)]
# alphabet = dict()
# result = 0
#
# if K < 5:
#     print(0)
# else:
#     alphabet['a'] = 1
#     alphabet['n'] = 1
#     alphabet['t'] = 1
#     alphabet['i'] = 1
#     alphabet['c'] = 1
#
#     recursion(K - 5)
#     print(result)
#


from itertools import combinations
import sys

input = sys.stdin.readline


def readable(word, alphabet):
    flag = True
    word = word[4:-4]
    for w in word:
        if w not in alphabet:
            flag = False
            break
    return flag


N, K = map(int, input().split())
word = []
for _ in range(N):
    word.append(input())

alphabet = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
must_alphabet = ['a', 'c', 'i', 'n', 't']
result = 0

if K < 5:
    print(0)
else:
    for c in combinations(alphabet, K - 5):
        cnt = 0
        for w in word:
            if readable(w, must_alphabet + list(c)):
                cnt += 1
        result = max(result, cnt)

    print(result)
