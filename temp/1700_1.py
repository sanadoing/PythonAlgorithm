N, K = map(int, input().split())

electronic = list(map(int, input().split()))
tap = [0] * N
result = 0

for i in range(len(electronic)):
    max_position = -1
    switch = 0
    if electronic[i] in tap:  # 이미 현재 전자 용품이 멀티탭에 꽂혀있는 경우
        continue
    elif 0 in tap:  # 멀티 탭에 자리가 있는 경우
        tap[tap.index(0)] = electronic[i]
    else:  # 멀티 탭에 자리가 다 찼을 경우, 멀티 탭에 있는 전기 용품 중에서 후에 쓰이지 않을 전기용품 또는 가장 늦게 쓰일 전기 용품을 찾아 자리를 바꿔준다.

        for j in range(len(tap)):
            if tap[j] not in electronic[i:]:
                switch = j
                break
            elif electronic[i:].index(tap[j]) > max_position:
                max_position = electronic[i:].index(tap[j])
                switch = j

    tap[switch] = electronic[i]
    result += 1

print(result)
