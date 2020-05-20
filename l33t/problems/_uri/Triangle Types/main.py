#!/usr/bin/env python

n1, n2, n3 = map(float, input().split(' '))
a, b, c = reversed(sorted([n1, n2, n3]))

if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:

    if ((a**2) == ((b**2) + (c**2))):
        print("TRIANGULO RETANGULO")

    if ((a**2) > ((b**2) + (c**2))):
        print("TRIANGULO OBTUSANGULO")

    if ((a**2) < ((b**2) + (c**2))):
        print("TRIANGULO ACUTANGULO")

    if (a == b and b == c):
        print("TRIANGULO EQUILATERO")

    if (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
        print("TRIANGULO ISOSCELES")
