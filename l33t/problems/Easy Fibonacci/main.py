#!/usr/bin/env python

from sys import stdin, stdout

F = [None] * 500001
F[0] = 0
F[1] = 1

gama = (10**8) + 7

for ii in range(2, 500001):
    F[ii] = (F[ii-1] + F[ii-2]) % gama

t = int(stdin.readline())

for tt in range(0, t):
    n = int(stdin.readline())
    stdout.write(str(F[n])+ "\n")
