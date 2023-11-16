for test_case in range(1, 11):
    cnt = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()
    for _ in range(cnt):
        if boxes[0] == boxes[-1]:
            break
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
    print(f'#{test_case} {boxes[-1] - boxes[0]}')
