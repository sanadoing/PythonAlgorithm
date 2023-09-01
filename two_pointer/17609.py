T = int(input())


def check(str_, left, right):
    while left < right:
        if str_[left] == str_[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


for i in range(T):
    str_ = str(input())
    left, right = 0, len(str_) - 1

    # 문자열 자체로 회문인 경우
    if str_ == str_[::-1]:
        print(0)
        continue
    while left < right:
        if str_[left] == str_[right]:
            left += 1
            right -= 1
        else:
            # 오른쪽 한 글자를 삭제
            remove_right = check(str_, left, right - 1)
            # 왼쪽 한 글자 삭제
            remove_left = check(str_, left + 1, right)

            # 유사 회문일 경우
            if remove_left or remove_right:
                print(1)
                break
            # 회문, 유사 회문 모두 아닐 경우
            else:
                print(2)
                break
