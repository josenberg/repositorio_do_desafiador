#!/usr/bin/env python

while True:
    a, b = [int(i) for i in input().split()]
    if (a == b):
        break;
    else:
        if (a > b):
            print("Decrescente")
        else:

            print("Crescente")
