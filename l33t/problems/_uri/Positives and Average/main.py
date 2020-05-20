#!/usr/bin/env python

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

count = 0
acc = 0

if (n1 > 0):
    count = count + 1
    acc = acc + n1

if (n2 > 0):
    count = count + 1
    acc = acc + n2

if (n3 > 0):
    count = count + 1
    acc = acc + n3

if (n4 > 0):
    count = count + 1
    acc = acc + n4

if (n5 > 0):
    count = count + 1
    acc = acc + n5

if (n6 > 0):
    count = count + 1
    acc = acc + n6

print(str(count) + ' valores positivos')
print('{:0.1f}'.format(acc/count))
