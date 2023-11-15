import sys

sys.setrecursionlimit(100000)

S = input()
T = input()
result = 0


def DFS(string):
    global result

    if string == S:
        print(1)
        exit(0)
    elif len(string) == 0:
        return
    else:
        if string[-1] == 'A':
            DFS(string[:-1])
        if string[0] == 'B':
            DFS(string[1:][::-1])


DFS(T)
print(0)
