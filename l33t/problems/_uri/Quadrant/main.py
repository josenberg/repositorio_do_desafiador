#!/usr/bin/env python

while True:
    x, y = [int(i) for i in input().split()]
    if (x == 0 or y == 0):
        break;
    else:
        if (x > 0 and y > 0):
            print('primeiro')
        elif(x > 0 and y < 0):
            print('quarto')
        elif(x<0 and y > 0):
            print('segundo')
        else:
            print('terceiro')
