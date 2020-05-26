#!/usr/bin/env python


k = int(input())

for kk in range(0, k):
    a, b = [int(x) for x in input().split()]

    acc = 0
    for n in range(min(a, b) + 1, max(a, b)):
        if (n % 2 == 1):
            acc = acc + n

    print(acc)
