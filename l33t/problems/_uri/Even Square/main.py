#!/usr/bin/env python


n = int(input())

for i in range(2, n+1, 2):
    print(str(i) + "^" + str(2) + " = " + str(i**2))
