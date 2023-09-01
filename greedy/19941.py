import sys

input = sys.stdin.readline

if __name__ == "__main__":

    N, K = map(int, input().split())
    PH = input()
    PH = list(PH)
    answer = 0
    for i in range(len(PH)):
        if PH[i] == "P":
            for j in range(i - K, i + K + 1):
                if 0 <= j <= N - 1 and PH[j] == "H":
                    answer += 1
                    PH[j] = "H_EAT"
                    break

    print(answer)
    # for i in range(len(PH)):
    #     if PH[i] == "P":
    #         # left
    #         idx = K
    #         while i != idx:
    #             if PH[i - K] == "H" and i - K > 0:
    #                 PH[i - K] = "H_EAT"
    #                 answer += 1
    #                 break
    #             idx += 1
    #
    #         else:
    #             # right
    #             idx = i
    #             while i + K != idx:
    #                 idx += 1
    #                 if idx > N-1:
    #                     break
    #                 if PH[idx] == "H" and idx < N - 1:
    #                     PH[idx] = "H_EAT"
    #                     answer += 1
    #                     break
    #     print(PH)
