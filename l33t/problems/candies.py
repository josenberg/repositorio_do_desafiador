#!/usr/bin/env python

k = int(input())

for kk in range(0, k):
    n = int(input())
    acc = 2
    i = 1
    while True:
        acc = acc * 2
        if (n % (acc - 1) == 0):
            print(int(n/(acc - 1)))
            break
