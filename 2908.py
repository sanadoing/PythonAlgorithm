n1, n2 = map(str, input().split())
n1 = list(n1)
n2 = list(n2)

for i in range(len(n1)):
    if int(n1[len(n1)-1-i]) > int(n2[len(n1)-1-i]):
        n1 = n1[::-1]
        print(''.join(map(str, n1)))
        break
    elif int(n1[len(n1)-1-i]) < int(n2[len(n1)-1-i]):
        n2 = n2[::-1]
        print(''.join(map(str, n2)))
        break
