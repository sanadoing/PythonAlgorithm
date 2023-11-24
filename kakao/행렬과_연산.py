from collections import deque


def solution(rc, operations):
    start = deque()
    mid = deque()
    end = deque()
    for i in rc:
        start.append(i[0])
        mid.append(deque(i[1:len(i) - 1]))
        end.append(i[len(i) - 1])

    for op in operations:
        if op == "Rotate":
            mid[0].appendleft(start.popleft())
            end.appendleft(mid[0].pop())
            mid[len(mid) - 1].append(end.pop())
            start.append(mid[len(mid) - 1].popleft())

        elif op == "ShiftRow":
            start.rotate()
            mid.rotate()
            end.rotate()

    answer = []
    for i in range(len(rc)):
        answer.append([start[i]] + list(mid[i]) + [end[i]])

    return answer
