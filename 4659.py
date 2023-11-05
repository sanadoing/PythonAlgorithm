while True:
    words = input()
    case1, case2, case3 = False, True, True
    if words == 'end':
        break
    else:
        cnt1, cnt2 = 0, 0  # 모음 갯수, 자음 갯수
        for i in range(len(words)):
            if words[i] in ['a', 'e', 'i', 'o', 'u']:
                case1 = True
                cnt1 += 1
                if cnt1 > 2:
                    case2 = False
                cnt2 = 0
            else:
                cnt2 += 1
                if cnt2 > 2:
                    case2 = False
                cnt1 = 0
            if i > 0 and words[i] == words[i - 1] and words[i] not in ['e', 'o']:
                case3 = False

    if case1 and case2 and case3:
        print(f'<{words}> is acceptable.')
    else:
        print(f'<{words}> is not acceptable.')
