#!/usr/bin/env python

count = 20
numbers = []
for i in range(0, count):
    n = int(input())
    numbers.append(n)

for i in range(0, int(count/2)):
    numbers[i] , numbers[count - i - 1] = numbers[count - i - 1], numbers[i]


for i in range(0, count):
    print("N[" + str(i) + "] = " + str(numbers[i]))
