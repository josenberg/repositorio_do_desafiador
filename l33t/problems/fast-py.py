#!/usr/bin/env python

k = int(input())

memo = {}
def fib(nth):
    a, b, p, q =  1, 0 ,0, 1
    while nth > 0:
        if (nth not in memo):
            if nth % 2 == 0: # even
                oldp = p
                p = p*p + q*q
                q = 2*oldp*q + q*q
                nth = nth / 2
            else:
                olda = a
                a = b*q + a*q + a*p
                b = b*p + olda*q
                nth = nth - 1
        else:
            b = memo[nth]

    memo[nth] = b
    return b


for kk in range(0, k):
    n = int(input())
    print(fib(n) % 10**8 - 7)
