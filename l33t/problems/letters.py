#!/usr/bin/env python
from bisect import bisect_left

n, m = map(int, input().split(' '))
levels = list(map(int, input().split(' ')))
letters = list(map(int, input().split(' ')))

def bSearch(ll, n):
    return bisect_left(ll, n)


true_levels = []
sum_l = 0
for level in levels:
    true_levels.append(sum_l)
    sum_l = sum_l + level

for letter in letters:
    floor = bSearch(true_levels, letter)
    print(str(floor) + " " + str(letter - true_levels[floor - 1]))
