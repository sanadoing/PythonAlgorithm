round = [4500, 1000, 25]
round_name = ["Round 1", "Round 2", "Round 3", "World Finals"]
T = int(input())
for t in range(T):
    N = int(input())
    for i in range(len(round)):
        if N > round[i]:
            print(f"Case #{t+1}: {round_name[i]}")
            break
    else:
        print(f"Case #{t + 1}: {round_name[3]}")
