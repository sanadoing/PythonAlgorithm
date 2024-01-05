l = []
max_length = 0
for _ in range(5):
    t = list(map(str,input()))
    max_length = max(max_length, len(t))
    l.append(t)
for i in range(max_length):
    for j in range(5):
        if len(l[j]) > i:
            print(l[j][i],end='')