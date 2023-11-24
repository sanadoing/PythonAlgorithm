from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)

    if (q1_sum + q2_sum) % 2 == 1:
        return -1

    for i in range(4 * n):
        if q1_sum == q2_sum:
            return i

        elif q1_sum > q2_sum:
            value = q1.popleft()
            q1_sum -= value

            q2.append(value)
            q2_sum += value
        else:
            value = q2.popleft()
            q2_sum -= value

            q1.append(value)
            q1_sum += value

    return -1