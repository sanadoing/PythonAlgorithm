P = int(input())

for _ in range(P):
    students = list(map(int, input().split()))
    result = 0
    new_students = []
    new_students.append(students[1])
    for i in range(2, 21):
        new_students.append(students[i])
        for j in range(len(new_students) - 1, 0, -1):
            if new_students[j] < new_students[j - 1]:
                result += 1
                new_students[j], new_students[j - 1] = new_students[j - 1], new_students[j]

    print(f'{students[0]} {result}')
