#!/usr/bin/env python
trsah = input()
numbers = list(map(int, input().split(' ')))

numbers.sort()
results = []

if (len(numbers) == 2):
    print(0)
else:
    first_possibility = numbers[-2] - numbers[0]
    second_possibility = numbers[-1] - numbers[1]
    if (first_possibility > second_possibility):
        print(second_possibility)
    else:
        print(first_possibility)
