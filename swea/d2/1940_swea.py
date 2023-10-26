T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    now_speed = 0
    result = 0

    for _ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 1:
            now_speed += command[1]
        elif command[0] == 2:

            now_speed -= command[1]
            if now_speed < 0:
                now_speed = 0

        result += now_speed

    print(f'#{test_case} {result}')
