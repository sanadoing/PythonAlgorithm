if __name__ == "__main__":
    n = int(input())
    cnt = 0
    dic = dict()

    for _ in range(n):
        idx = 0
        word = input()
        for w in word:
            if w in dic:
                if idx - dic[w] > 1:
                    break
            dic[w] = idx
            idx += 1
        else:
            cnt+=1
        print(dic)
        dic.clear()

    print(cnt)
