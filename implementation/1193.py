if __name__ == "__main__":
    n = int(input())

    count = 1
    summ = count
    while True:
        if n <= summ:
            break
        count += 1
        summ += count
    summ -= count

    if count%2==0:
        print(f"{n - summ}/{count - (n - summ) + 1}")
    else:
        print(f"{count - (n - summ) + 1}/{n - summ}")
