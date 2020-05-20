#!/usr/bin/env python
trash = input()
students = list(map(int, input().split(' ')))

students.sort()

problems = 0

for i, student in enumerate(students):
    if (i % 2 == 1):
        continue;

    problems = problems + (students[i + 1] - students[i])


print(problems)
