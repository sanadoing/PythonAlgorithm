if __name__ == "__main__":

    k = int(input())
    answer = 0
    l = []

    for i in range(k):
        x = int(input())
        if x == 0:
            l.pop()
        else:
            l.append(x)

    print(sum(l))
