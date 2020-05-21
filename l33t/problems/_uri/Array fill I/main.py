#!/usr/bin/env python

n = int(input())

for i in range(0, 10):
    print("N[" + str(i) + "] = " + str(n * (2**i)))
