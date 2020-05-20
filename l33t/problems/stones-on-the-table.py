#!/usr/bin/env python
trash = input()
raw_gems = input()

def isPositionValid(position, gems):
    return position >= 0 and position <= len(gems) - 1


def clearTable (gems):
    for i, gem in enumerate(gems):
        prv = None
        nxt = None
        if(isPositionValid(i - 1, gems)):
                prv = gems[i - 1]

        if(isPositionValid(i + 1, gems)):
                nxt = gems[i + 1]

        if ((prv != None and (prv == gem)) or
            (nxt != None and (nxt == gem))):
                return i

    return -1

anw = 0
while (True):
    gem_to_remove = clearTable(raw_gems)
    if (gem_to_remove == -1):
        break;
    else:
        anw = anw + 1
        raw_gems = raw_gems[:gem_to_remove] + raw_gems[gem_to_remove+1:]

print(anw)
