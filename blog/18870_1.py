N = int(input())
numbers = list(map(int, input().split()))
dic = dict()

numbers_sort = list(set(numbers))
numbers_sort.sort()

for i in range(len(numbers_sort)):
    dic[numbers_sort[i]] = i

for n in numbers:
    print(dic[n], end=' ')
