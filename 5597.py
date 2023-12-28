numbers = list([i+1 for i in range(30)])
for _ in range(28):
    n = int(input())
    numbers.remove(n)
for n in numbers:
    print(n)
