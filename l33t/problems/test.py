#!/usr/bin/env python
from bisect import bisect_left

def bSearch(ll, n):
    return bisect_left(ll, n)


n = int(input())

chapters = []
for nn in range(0, n):
    start, end = map(int, input().split(' '))
    chapters.append(end)

page = int(input())
current_chapter = bSearch(chapters, page)
print(len(chapters) - current_chapter)
