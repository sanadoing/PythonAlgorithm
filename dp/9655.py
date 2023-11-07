winner = ['SK', 'CY']
N = int(input())
result = -1
while N:

    if N >= 3:
        N -= 3
        result = (result + 1) % 2
    else:
        N -= 1
        result = (result + 1) % 2

print(winner[result])
