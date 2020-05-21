#!/usr/bin/env python

k = int(input())

count = 0
for kk in range(0, k):
    n = int(input())

    if (n >= 10 and n <= 20):
        count = count + 1

print(str(count) + " in")
print(str(k - count) + " out")
