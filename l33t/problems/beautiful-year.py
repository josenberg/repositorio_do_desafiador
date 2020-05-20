#!/usr/bin/env python

year = input()

year = str(int(year) + 1)

while True:
    year_digits = set()
    for digit in year:
        year_digits.add(digit)

    if (len(year_digits) == len(year)):
        print(year)
        break
    else:
        year = str(int(year) + 1)
