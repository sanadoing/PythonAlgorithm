p, m = map(int, input().split())
level, id = map(str, input().split())
rooms = []
rooms.append([(int(level), id)])

for _ in range(p - 1):
    level, id = map(str, input().split())

    for i in range(len(rooms)):
        if rooms[i][0][0] - 10 <= int(level) <= rooms[i][0][0] + 10 and len(rooms[i]) < m:
            rooms[i].append((int(level), id))
            break
    else:
        rooms.append([(int(level), id)])

for r in rooms:
    r.sort(key=lambda x: (x[1]))
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")

    for l, n in r:
        print(l, n)
