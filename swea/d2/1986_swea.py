T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    flag = False
    numbers = [1]
    if len(numbers) < N:
        for i in range(len(numbers), N):

            if flag:
                numbers.append(numbers[-1] + (i + 1))
                flag = False
            else:
                numbers.append(numbers[-1] - (i + 1))
                flag = True
    else:
        print(f'#{test_case} {numbers[N - 1]}')
        continue

    print(f'#{test_case} {numbers[N - 1]}')
