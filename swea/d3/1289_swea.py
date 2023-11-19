T = int(input())
for test_case in range(1, T + 1):
    memory = list(map(int, input()))
    result = 0
    now_memory = [0] * len(memory)
    for i in range(len(memory)):
        if memory[i] != now_memory[i]:
            result += 1
            for j in range(i, len(memory)):
                if now_memory[j] == 1:
                    now_memory[j] = 0
                else:
                    now_memory[j] = 1
    print(f'#{test_case} {result}')
