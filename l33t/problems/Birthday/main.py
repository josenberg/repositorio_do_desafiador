#!/usr/bin/env python
n = int(input())
numbers = list(map(int, input().split(' ')))
sorted_numbers = sorted(numbers)
rs = []
for i in range(0, len(numbers)):
    if (i % 2 == 0):
        rs.insert(0, sorted_numbers[i])
    else:
        rs.append(sorted_numbers[i])

for i in range(0, n):
    if (i + 1 == n):
        print(rs[i])
    else:
        print(rs[i], end = " ")
