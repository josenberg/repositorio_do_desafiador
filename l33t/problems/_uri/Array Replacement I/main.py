#!/usr/bin/env python

numbers = []
for i in range(0, 10):
    n = int(input())
    numbers.append(n)


for i in range(0, len(numbers)):
    if (numbers[i] <= 0):
        print("X[" + str(i) + "] = 1")
    else:
        print("X[" + str(i) + "] = " + str(numbers[i]))
