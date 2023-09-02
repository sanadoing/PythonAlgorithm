import sys

max_person = - sys.maxsize
sum_person = 0

for _ in range(10):
    out_person, in_person = map(int, input().split())
    sum_person = sum_person - out_person + in_person
    max_person = max(max_person, sum_person)

print(max_person)
