#!/usr/bin/env python

# Distinct Digits
# You have two integers l and r. Find an integer x
# which satisfies the conditions below: l≤x≤r.
# All digits of x are different.
# If there are multiple answers, print any of them.

entry = input()
l, r = map(int, entry.split())

def hasUniqDigits (n):
    word = str(n)
    s = set()
    for c in word:
        if (c in s):
            return False
        else:
            s.add(c)
    return True

ans = -1

for x in range(l, r + 1):
    if hasUniqDigits(x):
        ans = x
        break;

print(ans)
