#!/usr/bin/env python

a = int(input())
b = int(input())

acc = 0
for i in range(min(a, b), max(a,b) + 1):
    if (i % 13 is not 0):
        acc = acc + i

print(acc)
