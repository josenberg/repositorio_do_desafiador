#!/usr/bin/env python

n = int(input())
word = input()

n_count = 0
z_count = 0

for c in word:
    if (c == 'n'):
        n_count = n_count + 1
    if (c == 'z'):
        z_count = z_count + 1


for i in range(0, n_count):
    print("1", end = " ")


for i in range(0, z_count):
    print("0", end = " ")

print()
