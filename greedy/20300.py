if __name__ == "__main__":

    N = int(input())
    protein = list(map(int, input().split()))

    protein.sort()
    temp = []

    if len(protein) % 2 == 0:
        for i in range(len(protein) // 2):
            temp.append(protein[i] + protein[N - 1 - i])

        print(max(temp))
    else:
        for i in range(len(protein) // 2):
            temp.append(protein[i] + protein[N - 2 - i])

        temp.append(protein[-1])
        print(max(temp))
