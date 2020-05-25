#!/usr/bin/env python

n = input()

flag = False
for dig in range(len(n), 0, -1):
    if (flag == True):
        flag = False
        n[dig - 1] = str(int(n[dig - 1]) - 1)

    if (n[dig-1] == '0'):
        flag = True
        n[dig-1] = '9'

    print(n[dig-1])


print(n)
