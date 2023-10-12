from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = deque()
zero_cnt = 0
result = 0

for b in belt:
    if b == 0:
        zero_cnt += 1

while zero_cnt < K:

    # 벨트 한칸 씩 회전
    temp = belt[2 * N - 1]
    belt[1:] = belt[0:2 * N - 1]
    belt[0] = temp

    if len(robot) > 0:

        # 벨트 위의 로봇들도 따라 한칸 씩 회전
        for i in range(len(robot)):

            if robot[i] < N - 1:
                robot[i] += 1
                if robot[i] >= N - 1:
                    robot.remove(robot[i])
            else:
                robot.remove(robot[i])

        # 벨트 회전 후, 로봇이 앞으로 한칸 이동 (이동하려는 칸에 로봇x, 내구도 1이상)
        for i in range(len(robot) - 1, -1, -1):
            if belt[robot[i] + 1] >= 1 and robot[i] + 1 not in robot:
                robot[i] += 1
                belt[robot[i]] -= 1
                if belt[robot[i]] == 0:
                    zero_cnt += 1
                if robot[i] >= N - 1:
                    robot.remove(robot[i])

    if belt[0] > 0:
        robot.appendleft(0)
        belt[0] -= 1
        if belt[0] == 0:
            zero_cnt += 1

    result += 1

print(result)
