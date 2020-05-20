#!/usr/bin/env python
numbers = list(map(int, input().split(' ')))

sorted_numbers = sorted(numbers)

for i in sorted_numbers:
    print(i)
print()

for i in numbers:
    print(i)
