#!/usr/bin/env python

def isPerfect(n):
    n_list = list(str(n))
    count = 0
    for nn in n_list:
        count = count + int(nn)
    return count == 10


perfect_numbers = []
i = 0
n = 1
while (True):
    if (isPerfect(i)):
        perfect_numbers.append(i)
        print(str(i) + ',')
        if (len(perfect_numbers) == 10000):
            break;

    i = i + 1
