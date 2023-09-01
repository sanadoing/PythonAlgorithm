if __name__ == "__main__":
    S = input()
    T = input()

    TT = list(T)
    for _ in range(len(T)):
        if TT.pop() == 'B':
            TT = TT[::-1]
        else:
            TT = TT

        if len(TT) == len(S):
            break

    T = ''.join(TT)

    if T == S:
        print(1)
    else:
        print(0)
