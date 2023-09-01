from collections import deque

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):

        temp = input()
        length = int(input())
        s = input()
        num = []
        s = s[1:-1]
        if len(s) != 0:
            num = list(map(int, s.split(',')))

        r = temp.count('R')
        d = temp.count('D')

        if d > len(num):
            print('error')
            continue
        else:
            temp = list(temp[::-1])
            start = 0
            end = 0
            s = True
            while temp:
                if temp.pop() == 'R':

                    if s:
                        s = False
                    else:
                        s = True
                else:
                    if s:
                        start += 1
                    else:
                        end += 1

        num = num[start:len(num) - end]

        if r % 2 != 0:
            num = num[::-1]
        print(f"[{','.join(map(str, num))}]")
