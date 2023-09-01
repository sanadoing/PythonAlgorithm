if __name__ == "__main__":
    n, k = map(int, input().split())
    people = [i for i in range(1, n + 1)]
    answer = []
    idx = 0

    while len(answer) != n:
        idx += k - 1
        if idx >= len(people):
            idx = idx % len(people)
        answer.append(people.pop(idx))
    print("<" + str(answer)[1:-1] + ">")
    # answer = []
    # idx = 1
    # cnt = k
    # num = 0
    # while len(answer) != n:
    #
    #     while True:
    #         if cnt == 0:
    #             answer.append(num)
    #             cnt = k
    #             break
    #         num = int(idx % n)
    #         if num == 0:
    #             num = n
    #
    #         if num not in answer:
    #             idx += 1
    #             cnt -= 1
    #         else:
    #             idx += 1
    # print("<" + str(answer)[1:-1] + ">")
    print('<',end='')
    for i in range(n):
        if i == n-1:
            print(f"{answer[i]}", end='')
            break
        print(f"{answer[i]}, ", end='')

    print('>',end='')
