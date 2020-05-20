#!/usr/bin/env python
# 5 1
# 10 11 23 42 12
# 40 21
# --- respos
# 3 19
# 2 11
#


asw = []

def app():
    n, k = map(int, input().split(' '))
    students = list(map(int, input().split(' ')))

    distincts_students = {}

    for index, student in enumerate(students):
        if not(student in distincts_students):
            distincts_students[student] = index

        if (len(distincts_students) >= k):
            print('YES')
            for key in distincts_students:
                print((distincts_students[key] + 1), end = " ")
            print()
            return


    print('NO')
    return

app()
