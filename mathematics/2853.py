N = int(input())
List = []
for _ in range(N):
    x = int(input())
    List.append(x)

cnt = 0
List.pop(0)

while True:
    if len(List) == 0:
        break
    temp = List[0] - 1
    for i in range(1, List[-1]+1, temp):
        # print(i)
        # for x in List:
        #     if i == x:
        if i != 1:
            List.remove(i)

    cnt += 1

print(cnt)




