#!/usr/bin/env python

ih, im, fh, fm = map(int, input().split(' '))
rh = 0
if (ih > fh):
    fh = fh + 24
rh = fh - ih

if (rh == 0 and im > fm):
    rh = 24

if (im > fm):
    rh = rh - 1
    fm = fm + 60
rm = fm - im

if (rh == 0 and rm == 0):
    rh = 24


print("O JOGO DUROU " + str(rh) + " HORA(S) E "+ str(rm) + " MINUTO(S)")
