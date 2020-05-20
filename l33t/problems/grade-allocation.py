#!/usr/bin/env python
t = int(input())
for times in range(0, t):
    n, m = list(map(int, input().split(' ')))
    students = list(map(int, input().split(' ')))

    needed_score = m - students[0]

    others_scores = 0
    for i in range(1, len(students)):
         others_scores = others_scores + students[i]

    if (others_scores >= needed_score):
        print(m)
    else:
        print(students[0] + others_scores)
