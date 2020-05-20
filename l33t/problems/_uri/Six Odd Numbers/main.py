#!/usr/bin/env python

n = int(input())

for i in range(0, 12, 2):
    if ((n + i) % 2 == 0):
        print(n + i + 1)
    else:
        print(n + i)
