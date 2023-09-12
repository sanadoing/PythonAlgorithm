import sys

def recursion(idx, result):
    global max_number, min_number
    global plus, minus, mul, div

    if idx == len(number):
        max_number = max(max_number, result)
        min_number = min(min_number, result)
        return
    else:
        if plus > 0:
            plus -= 1
            recursion(idx + 1, result + number[idx])
            plus += 1

        if minus > 0:
            minus -= 1
            recursion(idx + 1, result - number[idx])
            minus += 1

        if mul > 0:
            mul -= 1
            recursion(idx + 1, int(result * number[idx]))
            mul += 1

        if div > 0:
            div -= 1
            recursion(idx + 1, int(result / number[idx]))
            div += 1



N = int(input())
number = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_number = -sys.maxsize
min_number = sys.maxsize
result = number[0]
recursion(1, result)

print(max_number)
print(min_number)

