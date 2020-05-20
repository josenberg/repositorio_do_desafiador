#!/usr/bin/env python
n = int(input())

userbase = {}
for trash in range(0, n):
    user = input()
    if not(user in userbase):
        userbase[user] = 0
        print('OK')
    else:
        userbase[user] = userbase[user] + 1
        print(user + str(userbase[user]))
