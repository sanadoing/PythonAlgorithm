
if __name__ == "__main__":

    n = int(input())
    answer = [0 for i in range(n)]
    data = [list(map(int,input().split())) for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                cnt += 1
        answer[i] = cnt
        cnt = 1
    for i in range(n):
        print(answer[i], end=' ')
