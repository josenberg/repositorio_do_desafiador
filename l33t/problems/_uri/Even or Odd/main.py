#!/usr/bin/env python

n = int(input())

for nn in range(0, n):
    x = float(input())

    signal = 'NEGATIVE'
    isNull = False
    typee = 'ODD'

    if (x == 0):
        print('NULL')
    else:
        if (x > 0):
            signal = 'POSITIVE'
        if (x % 2 == 0):
            typee = 'EVEN'

        print(typee + " " + signal)
