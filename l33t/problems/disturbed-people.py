#!/usr/bin/env python
t = int(input())
numbers = list(map(int, input().split(' ')))

rs = 0
for i in range(1, len(numbers) - 1):
    if (numbers[i] == 0 and numbers[i - 1] == 1 and numbers[i + 1] == 1):
        rs = rs + 1
        numbers[i+1] = 0

print(rs)
