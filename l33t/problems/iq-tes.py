#!/usr/bin/env python

trash = input()
numbers = list(map(int, input().split(' ')))

q_even = 0
q_odd = 0

last_odd = None
last_even = None

for index, number in enumerate(numbers):
  if (number % 2):
    q_even = q_even + 1
    last_even = index
  else:
    q_odd = q_odd + 1
    last_odd = index


  if (q_even >= 2 and last_odd != None):
    print(last_odd + 1)
    break

  if (q_odd >= 2 and last_even != None):
    print(last_even + 1)
    break
