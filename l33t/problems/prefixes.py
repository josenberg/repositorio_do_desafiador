#!/usr/bin/env python
n = int(input())
word = list(input())

count = 0
for i in range(0, n, 2):
    curr, nxt = word[i], word[i + 1]
    if (curr == nxt and curr == 'b'):
        count = count + 1
        word[i] = 'a'

    if (curr == nxt and curr == 'a'):
        count = count + 1
        word[i] = 'b'


print(str(count))
print("".join(word))
