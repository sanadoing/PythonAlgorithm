if __name__ == "__main__":
    str1 = input()
    str2 = list(map(str, str1.split('.')))
    str3 = list(map(str, str1.split('X')))

    temp = ''
    answer = ''

    str_x = []
    str_dot = []

    idx_x = 0
    idx_dot = 0

    for w in range(len(str2)):  # str_x 리스트에 X로 구성된 문자열만 저장
        if str2[w] != '':
            str_x.append(str2[w])

    for q in range(len(str3)):  # str_dot 리스트에 .로 구성된 문자열만 저장
        if str3[q] != '':
            str_dot.append(str3[q])

    for i in range(len(str_x)):
        if int(len(str_x[i]) % 2) != 0:     # X의 수가 홀수개면 AAAA 또는 BB 로 덮을 수 없기에 -1 출력
            print(-1)
            break
        elif int(len(str_x[i]) % 4) == 0:      # X의 수가 4로 나눈 나머지가 0, AAAA 로만 덮을 수 있는 경우
            for _ in range(int(len(str_x[i]) / 4)):
                temp += 'AAAA'

        else:
            if int(len(str_x[i]) / 4) >= 1:      # X의 수가 4로 나눈 나머지가 0보다 크면 , AAAA와 BB로 덮을 수 있는 경우
                for _ in range(int(len(str_x[i]) / 4)):     # AAAA로 먼저 덮은 후
                    temp += "AAAA"

                for _ in range(int(len(str_x[i]) % 4 / 2)):     # BB로 덮기
                    temp += "BB"
            else:
                for _ in range(int(len(str_x[i]) / 2)):      # X의 수가 4로 나눈 나머지가 0보다 작으면 , BB로만 덮을 수 있는 경우
                    temp += "BB"
        str_x[i] = temp
        temp = ''
    else:
        if str1[0] == '.':      # 주어진 문자열의 첫 문자가 .으로 이루어 졌을 경우
            for i in range(1, len(str_x) + len(str_dot) + 1):
                if int(i % 2) != 0:
                    answer += str_dot[idx_dot]
                    idx_dot += 1
                else:
                    answer += str_x[idx_x]
                    idx_x += 1
        else:      # 주어진 문자열의 첫 문자가 X으로 이루어 졌을 경우
            for i in range(1, len(str_x) + len(str_dot) + 1):
                if int(i % 2) == 0:
                    answer += str_dot[idx_dot]
                    idx_dot += 1
                else:
                    answer += str_x[idx_x]
                    idx_x += 1

        print(answer)
