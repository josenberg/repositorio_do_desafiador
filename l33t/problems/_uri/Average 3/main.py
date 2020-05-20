#!/usr/bin/env python
#
import math

n1, n2, n3, n4 = map(float, input().split(' '))
avg = ((n1 * 2.0) + (n2 * 3.0) + (n3 * 4.0) + n4)/10.0

print('Media: {:0.1f}'.format(avg))
if (avg >= 7.0):
    print('Aluno aprovado.')
elif (avg < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exam = float(input())
    new_avg = (exam + avg)/2.0
    new_avg = round(new_avg, 1)
    if (new_avg < 5.0):
        print('Aluno reprovado.')
        print('Media final: {:0.1f}'.format(new_avg))
    else:
        print('Aluno aprovado.')
        print('Media final: {:0.1f}'.format(new_avg))
