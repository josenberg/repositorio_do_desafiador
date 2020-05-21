#!/usr/bin/env python

bigger = None
bigger_index = None

for i in range(0, 100):
    n = int(input())
    if (bigger == None or n > bigger):
        bigger = n
        bigger_index = i + 1

print(bigger)
print(bigger_index)
