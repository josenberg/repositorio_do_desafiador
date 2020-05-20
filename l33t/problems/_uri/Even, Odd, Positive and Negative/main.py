#!/usr/bin/env python

numbers = []
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))
numbers.append(int(input()))

odd, even, negative, positive = 0, 0, 0, 0

for number in numbers:
    if (number % 2 == 0):
        even = even + 1
    else:
        odd = odd + 1

    if (number > 0):
        positive = positive + 1

    if (number < 0):
        negative = negative + 1

print(str(even) + ' valor(es) par(es)')
print(str(odd) + ' valor(es) impar(es)')
print(str(positive) + ' valor(es) positivo(s)')
print(str(negative) + ' valor(es) negativo(s)')
