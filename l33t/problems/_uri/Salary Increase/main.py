#!/usr/bin/env python

n = float(input())

if(n <= 400.0):
    new_n = n * 1.15
    delta_n = new_n - n
    percentage = 15
elif(n <= 800.0):
    new_n = n * 1.12
    delta_n = new_n - n
    percentage = 12
elif(n <= 1200.0):
    new_n = n * 1.10
    delta_n = new_n - n
    percentage = 10
elif(n <= 2000.0):
    new_n = n * 1.07
    delta_n = new_n - n
    percentage = 7
else:
    new_n = n * 1.04
    delta_n = new_n - n
    percentage = 4

print('Novo salario: {:0.2f}'.format(new_n))
print('Reajuste ganho: {:0.2f}'.format(delta_n))
print('Em percentual: ' + str(percentage) + ' %')
