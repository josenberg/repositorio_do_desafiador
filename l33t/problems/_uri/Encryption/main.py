#!/usr/bin/env python
x = int(input())

for xx in range(0, x):
    word = list(input())
    for i in range(0, len(word)):
        if (word[i].isalpha()):
            word[i] = chr(ord(word[i]) + 3)

    word = list(reversed(word))
    for i in range(int(len(word) / 2), len(word)):
        word[i] = chr(ord(word[i]) - 1)

    print("".join(word))
