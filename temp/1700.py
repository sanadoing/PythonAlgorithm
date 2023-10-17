N, K = map(int, input().split())
electronic = list(map(int, input().split()))

multitap = [0] * N
result = 0

for i, e in enumerate(electronic):
    max_position = -1
    change = 0
    if e in multitap:
        continue
    elif 0 in multitap:
        multitap[multitap.index(0)] = e
    else:
        # 이미 모든 자리에 꽂혀있는 멀티탭에서 우선순위를 정해 우선순위가 가장 낮은 전자기기를 빼려고 함.
        for m in multitap:
            # 만약 현재 전자기기의 인덱스 번호 이후에 더이상 사용될 전자기기가 없는 경우.
            if m not in electronic[i:]:
                # 그 멀티탭에 꽂혀있는 전자기기를 빼고 현재의 전자기기를 넣는다.
                change = m
                break
            # 만약 현재 전자기기의 인덱스 번호 이후에 모든 전자기기가 다 사용될 경우. => 가장 늦게 사용될 전자기기를 찾는다.  --- (2)
            elif electronic[i:].index(m) > max_position:
                max_position = electronic[i:].index(m)
                change = m

        # (2)의 경우 ! : 현재 멀티탭에 꽂혀있는 전자기기 중에 나중에 쓰이지 않을 전자기기가 없는 경우, 가장 늦게 사용될 전자기기를 빼고 그자리에 현재 전자기기를 꽂아준다.
        multitap[multitap.index(change)] = e
        result += 1

print(result)
