#!/usr/bin/env python
#  A - Petya and Origami
#  Petya is having a party soon, and he has decided to invite his n friends.
# He wants to make invitations in the form of origami. For each invitation, he needs two red sheets, five green sheets, and eight blue sheets. The store sells an infinite number of notebooks of each color, but each notebook consists of only one color with k
# sheets. That is, each notebook contains k sheets of either red, green, or blue.
# Find the minimum number of notebooks that Petya needs to buy to invite all n
# of his friends.


import math

entry = input()
friends, pack = entry.split()

number_of_friends = int(friends)
sheets_per_pack = int(pack)

need_red = 2 * number_of_friends
need_green = 5 * number_of_friends
need_blue = 8 * number_of_friends

number_of_books = math.ceil(need_red / sheets_per_pack) + math.ceil(need_green / sheets_per_pack) + math.ceil(need_blue / sheets_per_pack)

print(number_of_books)
