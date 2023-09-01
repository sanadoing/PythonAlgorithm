X, Y, W, S = map(int, input().split())
result = 0

minn = min(X, Y)
maxx = max(X, Y)

if 2 * W >= S:  # 가로 한번 세로 한번 가는게 대각선으로 한번 가는 것보다 더 오래 걸릴 경우

    #   대각선 한번이 가로 나 세로 한번보다 빠를 경우
    if W >= S:
        result += minn * S
        if (maxx - minn) % 2 == 0:
            result += (maxx - minn) * S
        else:

            result += ((maxx - minn) // 2) * S * 2
            result += ((maxx - minn) % 2) * W
    else:
        result += minn * S
        result += (maxx - minn) * W

else:  # 대각선으로 가는게 더 빠를 경우
    result += minn * 2 * W
    result += (maxx - minn) * W

print(result)
