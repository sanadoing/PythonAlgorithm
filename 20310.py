S = input()
z_cnt = S.count('0') // 2
o_cnt = S.count('1') // 2
temp_z = 0
flag = False
for i in range(len(S)):
    if S[i] == '1':
        if o_cnt:
            o_cnt -= 1
        else:
            print(S[i], end="")
    else:
        temp_z += 1
        if flag == False:
            print(S[i], end="")
        if temp_z == z_cnt:
            flag = True
