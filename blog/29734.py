N, M = map(int, input().split())
T, S = map(int, input().split())
zip, dok = 0, 0
if N % 8 == 0:
    zip = (8 + S) * (N // 8 - 1) + 8
else:
    zip = (8 + S) * (N // 8) + N % 8
if M % 8 == 0:
    dok = (2 * T + 8 + S) * (M // 8 - 1) + (T + 8)
else:
    dok = (2 * T + 8 + S) * (M // 8) + (T + M % 8)
if zip <= dok:
    print("Zip")
    print(zip)
else:
    print("Dok")
    print(dok)
