N = int(input())
study = []
joon = []

for _ in range(N):
    string = input()
    if 'boj.kr/' in string:
        link, number = string.split('/')
        if number.isdigit():
            joon.append([string, int(number)])
        else:
            study.append(string)
    else:
        study.append(string)
study.sort(key=lambda x: (len(x), x))
joon.sort(key=lambda x: (x[1]))
for s in study:
    print(s)
for j in joon:
    print(j[0])
