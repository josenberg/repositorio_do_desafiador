#!/usr/bin/env python

a = int(input())
b = int(input())

count = 0
for i in range(min(a,b) + 1, max(a,b)):
    if (i % 2 == 1):
        count = count + i


print (count)
