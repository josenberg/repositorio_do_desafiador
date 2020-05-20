#!/usr/bin/env python
# - Less or Equal
# You are given a sequence of integers of length n and integer number k. You should print any integer number x in the range of [1;109] (i.e. 1≤x≤109) such that exactly k elements of given sequence are less than or equal to x
# Note that the sequence can contain equal elements.
# If there is no such x, print "-1" (without quotes).

n, k = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

numbers.sort()

k = k - 1

if (k < 0):
    if (numbers[0] > 1):
        print(1)
    else:
        print(-1)
else:
    if (len(numbers) > k+1 and numbers[k] == numbers[k+1]):
        print(-1)
    else:
        print(numbers[k])
