#!/usr/bin/env python

import math

a, b, c = map(float, input().split(' '))
p = (a + b + c)/2

if (a+b <= c or a+c <= b or b+c <= a):
    s = (min(a, b) * c) + ((abs(a - b) * c)/2)
    print('Area = {:0.1f}'.format(s))
else:
    print('Perimetro = {:0.1f}'.format(p*2))
