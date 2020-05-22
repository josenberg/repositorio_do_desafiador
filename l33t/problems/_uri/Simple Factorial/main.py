#!/usr/bin/env python

fac = [1]
for i in range(1, 13):
    fac.append(fac[i-1] * i)


n = int(input())
print(fac[n])
