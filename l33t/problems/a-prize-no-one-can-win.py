#!/usr/bin/env python

n, max_price = map(int, input().split(' '))
prices = sorted(list(map(int, input().split(' '))))

answer = 0
acc = 0

for i in range(1, n):
    acc = prices[i - 1] + prices[i]
    if (acc <= max_price):
        answer = i
    else:
        break

print(answer + 1)
