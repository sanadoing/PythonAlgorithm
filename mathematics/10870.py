N = int(input())
fib = [0] * N
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    fib[0], fib[1] = 1, 1

    for i in range(2, N):
        fib[i] = fib[i - 1] + fib[i - 2]

    print(fib[N - 1])
