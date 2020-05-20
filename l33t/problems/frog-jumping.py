#!/usr/bin/env python
import math

t = int(input())

for i in range(0, t):
    a, b, k = map(int, input().split(' '))
    result = (a * math.ceil(k / 2)) - (b * math.floor(k / 2))
    print(str(result))
