#!/usr/bin/env python
import math
entries = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'  ]

for i in range(0, entries):
    ans = ''
    size, number = map(int, input().split(' '))
    freq = math.floor(size / number)
    m = size % number

    for a in range(0, size):
        ans = ans + str(chr(a % number + 97))

    print(ans)
