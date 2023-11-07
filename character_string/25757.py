dic = {'Y': 1, 'F': 2, 'O': 3}
N, game = map(str, input().split())
N = int(N)
members = set(list(input() for _ in range(N)))
print(len(members)//dic[game])
