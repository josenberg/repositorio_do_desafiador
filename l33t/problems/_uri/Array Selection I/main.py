#!/usr/bin/env python

count = 100
nn = []
for i in range(0, count):
    n = float(input())
    nn.append(n)

for i in range(0, count):
    if(nn[i] <= 10.0):
        print("A[" + str(i) + "] = " + str(nn[i]))
