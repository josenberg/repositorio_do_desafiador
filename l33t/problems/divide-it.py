#!/usr/bin/env python
q = int(input())

for qq in range(0, q):
    n = int(input())
    counter = 0
    while (n != 1):
        counter = counter + 1
        if (n % 2 == 0):
            n = n // 2
        elif (n % 3 == 0):
            n = 2*n // 3
        elif (n % 5 == 0):
            n = (4*n) // 5
        else:
            counter = -1
            break;

    print(str(counter))
