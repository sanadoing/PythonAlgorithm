from collections import defaultdict

T = int(input())
for _ in range(T):
    string = input()
    k = int(input())
    dic = defaultdict(list)
    temp = []
    min_result, max_result = len(string)+1, -1
    for i, s in enumerate(string):
#         문자별로 인덱스 저장해서 큰값 작은 값 출력
        if s not in dic:
            dic[s] = [i]
        else:
            dic[s].append(i)
        if len(dic[s]) >= k:
            temp.append(s)

    temp = list(set(temp))

    for t in temp:
        for i in range(len(dic[t])-k+1):
            min_result = min(min_result, dic[t][i+k-1]-dic[t][i]+1)
            max_result = max(max_result, dic[t][i+k-1]-dic[t][i]+1)
    if min_result == len(string)+1:
        print(-1)
    else:
        print(min_result, max_result)
