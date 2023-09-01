if __name__ == "__main__":
    n, m = map(int, input().split())
    j = int(input())
    answer = 0
    position_f = 1      # 바구니의 앞부분 위치
    position_b = m      # 바구니의 뒷부분 위치

    for _ in range(j):
        apple = int(input())
        if position_f <= apple and apple <= position_b:
            answer += 0
        elif position_b < apple:
            answer += apple - position_b
            position_b = apple
            position_f = position_b - (m - 1)
        elif apple < position_f:
            answer += position_f - apple
            position_f = apple
            position_b = position_f + (m - 1)

    print(answer)
