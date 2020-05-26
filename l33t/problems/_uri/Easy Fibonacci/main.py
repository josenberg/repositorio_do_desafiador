#!/usr/bin/env python

fib = []
fib.append(0)
fib.append(1)

for i in range(2, 47):
    fib.append(fib[i - 2] + fib[i - 1])

n = int(input())

for i in range(0, n):
    if (i == n - 1):
        print(fib[i])
    else:
        print(fib[i], end=" ")
