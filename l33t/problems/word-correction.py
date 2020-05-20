#!/usr/bin/env python

trash = input()
word = input()

vowels = set(['a', 'e', 'i', 'o', 'u', 'y' ])

new_word = ''

for i in range(0, len(word)):
    current = word[i]
    prev = word[i - 1] if i - 1 >= 0 else None
    if not(current in vowels and prev in vowels):
        new_word = new_word + current


print(new_word)
