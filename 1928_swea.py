T = int(input())
dic = dict()
for i in range(ord('A'), ord('Z')+1):
    dic[chr(i)] = i - 65
for i in range(ord('a'), ord('z')+1):
    dic[chr(i)] = i - 71
for i in range(10):
    dic[str(i)] = 52 + i
dic['+'], dic['/'] = 62, 63

for test_case in range(1, T + 1):
    string = input()
    temp = ""
    for s in string:
        temp += "".join(format(dic[s], 'b').zfill(6))
    result = ""
    for i in range(0, len(temp), 8):
        result += chr(int(temp[i:i+8], 2))

    print(f"#{test_case} {result}")
