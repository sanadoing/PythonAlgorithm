while True:
    string = input()
    if string == 'end':
        break
    else:
        x_cnt = string.count('X')
        o_cnt = string.count('O')
        d_cnt = string.count('.')
        if o_cnt <= x_cnt and x_cnt - o_cnt <= 1:
            ox = []
            for i in range(3):
                #   가로
                if (string[i * 3] == string[(i * 3) + 1] == string[(i * 3) + 2]) and string[i * 3] != '.':
                    ox.append(string[i * 3])
                #   세로
                if (string[i] == string[i + 3] == string[i + 6]) and string[i] != '.':
                    ox.append(string[i])
            #   대각선
            if string[0] == string[4] == string[8] and string[4] != '.':
                ox.append(string[4])
            if string[2] == string[4] == string[6] and string[4] != '.':
                ox.append(string[4])
            if len(ox) == 0 and d_cnt == 0:
                print("valid")
            elif len(ox) == 1:
                if (ox[0] == 'O' and x_cnt <= o_cnt) or (ox[0] == 'X' and x_cnt != o_cnt):
                    print("valid")
                elif d_cnt == 0 and ox[0] == 'X':
                    print("valid")
                else:
                    print("invalid")
            elif len(ox) == 2 and d_cnt == 0 and ox[0] == ox[1] == 'X':
                print("valid")
            else:
                print("invalid")

        else:
            print("invalid")
