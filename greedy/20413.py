if __name__ == "__main__":
    month = int(input())
    money = list(map(int, input().split()))
    grade = input()

    prev = 0
    result = 0

    for g in grade:

        if g == 'B':
            result += money[0] - prev - 1
            prev = money[0] - prev - 1
        elif g == 'S':
            result += money[1] - prev - 1
            prev = money[1] - prev - 1
        elif g == 'G':
            result += money[2] - prev - 1
            prev = money[2] - prev - 1
        elif g == 'P':
            result += money[3] - prev - 1
            prev = money[3] - prev - 1
        else:
            result += money[3]
            prev = money[3]

        print(result, prev)


    print(result)