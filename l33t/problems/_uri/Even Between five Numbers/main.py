#!/usr/bin/env python

numbers = []
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))

even = 0
for number in numbers:
    if (number % 2 == 0):
        even = even + 1

print(str(even) + ' valores pares')
