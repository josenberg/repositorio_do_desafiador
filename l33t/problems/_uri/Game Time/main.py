#!/usr/bin/env python

start, end = map(int, input().split(' '))

if (end > start):
    x = end - start
elif(end == start):
    x = 24
else:
    x = end + 24 - start

print("O JOGO DUROU " + str(x) + " HORA(S)")
