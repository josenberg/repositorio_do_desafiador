#!/usr/bin/env python

# - Snacktower
# According to an old legeng, a long time ago Ankh-Morpork residents did something wrong to miss Fortune, and she cursed them. She said that at some time n snacks of distinct sizes will fall on the city, and the residents should build a Snacktower of them by placing snacks one on another. Of course, big snacks should be at the bottom of the tower, while small snacks should be at the top.
# Years passed, and once different snacks started to fall onto the city, and the residents began to build the Snacktower.
# However, they faced some troubles. Each day exactly one snack fell onto the city, but their order was strange. So, at some days the residents weren't able to put the new stack on the top of the Snacktower: they had to wait until all the bigger snacks fell. Of course, in order to not to anger miss Fortune again, the residents placed each snack on the top of the tower immediately as they could do it.
# Write a program that models the behavior of Ankh-Morpork residents.
#
# -- input
#    The first line contains single integer n (1 ≤ n ≤ 100 000) — the total number of snacks.
#    The second line contains n integers, the i-th of them equals the size of the snack which fell on the i-th day. Sizes are distinct integers from 1 to n.
# -- output
#   Print n lines. On the i-th of them print the sizes of the snacks which the residents placed on the top of the Snacktower on the i-th day in the order they will do that. If no snack is placed on some day, leave the corresponding line empty.

days = int(input())
entry = input()
snacks = list(map(int, entry.split(" ")))

store = [None] * days

for i, snack in enumerate(snacks):
    store_position = snack - 1
    if (snack == days):
        print(snack, end = ' ');
        days = days - 1
        while(store[store_position - 1] != None and store_position > -1):
            print(store[store_position - 1], end = " ")
            store_position = store_position - 1
            days = days - 1
        print("")
    else:
        store[store_position] = snack
        if (snack != snacks[-1]):
            print("")

need_print = False
for i in range(days - 1, 0, -1):
    need_print = True
    print(i, end = ' ')

if (need_print):
    print("")
