#!/usr/bin/env python
#
def isEquivalent (a, b):
    size = len(a)
    if (a == b):
        return True
    if (size % 2 == 1):
        return False
   
    a1 = a[size//2:]
    a2 = a[0:size//2]

    b1 = b[size//2:]
    b2 = b[0:size//2]

    if (size <= 2):
      return (a1 == b1 and a2 == b2) or (a1 == b2 and a2 == b1)
    else:
      return (
          (isEquivalent(a1, b2) and isEquivalent(a2, b1))
          or
          (isEquivalent(a1, b1) and isEquivalent(a2, b2))
      )


aa = input()
bb = input()


if (isEquivalent(aa, bb)):
    print('YES')
else:
    print ('NO')
