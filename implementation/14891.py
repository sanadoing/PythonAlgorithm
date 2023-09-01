if __name__ == "__main__":

    wheel = []
    wheel.append([0, 0, 0, 0, 0, 0, 0, 0])
    score = [1, 2, 4, 8]
    result = 0

    for _ in range(4):
        temp = list(map(int, input()))
        wheel.append(temp)

    k = int(input())
    for i in range(k):
        num, t = map(int, input().split())
        # left

        turn = [0] * 5
        turn[num] = t
        a, b = num - 1, num  # a 는 왼쪽 바퀴, b는 오른쪽 바퀴
        while a > 0:
            if wheel[a][2] != wheel[b][6]:
                turn[a] = turn[b] * -1
            else:
                break

            a, b = a - 1, b - 1
        # right
        a, b = num, num + 1
        while b < 5:
            if wheel[a][2] != wheel[b][6]:
                turn[b] = turn[a] * -1
            else:
                break
            a, b = a + 1, b + 1

        for i in range(1, 5):

            if turn[i] == 1:
                temp = wheel[i][7]
                wheel[i][1:8] = wheel[i][0:7]
                wheel[i][0] = temp

            if turn[i] == -1:
                temp = wheel[i][0]
                wheel[i][0:7] = wheel[i][1:8]
                wheel[i][7] = temp


    for i in range(4):
        result += wheel[i+1][0] * score[i]

    print(result)
