#!/usr/bin/env python
places, dest = map(int, input().split(' '))

portals = list(map(int, input().split(' ')))

current_position = 1

visited = set()

visited.add(current_position)
while (current_position < places):
    portal = portals[current_position - 1]
    current_position = current_position + portal
    visited.add(current_position)

print("YES") if (dest in visited) else print("NO")
