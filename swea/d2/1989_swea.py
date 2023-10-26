T = int(input())

for test_case in range(1, T + 1):
    word = input()
    for i in range(len(word)//2):
        if word[i] != word[len(word)-(i + 1)]:
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} 1')