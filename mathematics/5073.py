while True:
    a, b, c = map(int, input().split())
    if (a and b and c) == 0:
        break
    else:
        if a == b == c:
            print("Equilateral")
        else:
            if max(a, b, c) >= (a + b + c) - max(a, b, c):
                print("Invalid")
            else:
                if (a == b) or (b == c) or (a == c):
                    print("Isosceles")
                else:
                    print("Scalene")

