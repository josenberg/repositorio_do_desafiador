#!/usr/bin/env python

while True:
    m, n = [int(i) for i in input().split()]
    if (m <= 0 or n <= 0):
        break;
    else:
        acc = 0
        for i in range(min(m, n), max(m, n) + 1):
            acc = acc + i
            print(i ,end=' ' )
        print("Sum=" + str(acc))
