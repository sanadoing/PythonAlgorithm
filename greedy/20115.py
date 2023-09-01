if __name__ == "__main__":
    n = int(input())
    drink = list(map(int, input().split()))

    drink.sort(reverse=True)

    while True:
        drink[0] = drink[0] + drink.pop()/2
        if len(drink) == 1:
            break

    print(drink[0])
