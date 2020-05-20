#!/usr/bin/env python

prices = [
    4.00,
    4.50,
    5.00,
    2.00,
    1.50,
]

n, q = map(int, input().split(' '))
print('Total: R$ {:0.2f}'.format(prices[n - 1] * q))
