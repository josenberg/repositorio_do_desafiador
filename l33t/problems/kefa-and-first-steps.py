#!/usr/bin/env python
n = int(input())
dayz = list(map(int, input().split(' ')))

counter = 1
biggest = 1

for i in range(1, n):
    if dayz[i] >= dayz[i - 1]:
        counter = counter + 1
    else:
        counter = 1

    if (counter > biggest):
        biggest = counter


print(biggest)
