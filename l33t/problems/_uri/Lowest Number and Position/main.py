#!/usr/bin/env python

c = int(input())
nn = [int(i) for i in input().split()]


smallest = nn[0]
smallest_index = 0
for i in range(1, len(nn)):
    if (nn[i] < smallest):
        smallest = nn[i]
        smallest_index = i

print("Menor valor: " + str(smallest))
print("Posicao: " + str(smallest_index))
