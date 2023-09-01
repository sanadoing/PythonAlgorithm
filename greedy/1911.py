N, L = map(int, input().split())

puddle = []
for _ in range(N):
    s, e = map(int, input().split())
    puddle.append((s, e))

puddle.sort()

point = 0       # 널빤지로 웅덩이를 가리고 나서, 그 널빤지의 가장 끝 지점을 저장할 변수 -> 그 다음 웅덩이를 가릴 수도 있기 때문에
result = 0

for i in range(N):
    s, e = puddle[i][0], puddle[i][1]

    if point > s:  # 전에 걸친 널빤지가 다음 웅덩이의 일부분을 덮을 경우
        s = point

    cnt = (e - s) // L

    if (e - s) % L != 0:    # 널빤지를 걸쳤는데, 아직 웅덩이가 덜 가려졌을 경우 그 남은 웅덩이는 널빤지 하나 길이보단 짧다.
        cnt += 1
        point = s + L * cnt
    else:
        point = e

    result += cnt

print(result)
