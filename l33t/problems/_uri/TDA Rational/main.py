#!/usr/bin/env python

'''
Sum: (N1*D2 + N2*D1) / (D1*D2)
Subtraction: (N1*D2 - N2*D1) / (D1*D2)
Multiplication: (N1*N2) / (D1*D2)
Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)
'''

def simpl(n, d):
    i = 2

    if (n == 0):
        return [0, 1]

    while (abs(n) >= i and abs(d) >= i):
        if (n % i == 0 and d % i == 0):
            n = n/i
            d = d/i
        else:
            i = i + 1
    return [int(n), int(d)]

def sum(n1, d1, n2, d2):
    n_n = (n1*d2 + n2*d1)
    n_d = d1*d2
    sim = simpl(n_n, n_d)
    sim_rs = str(sim[0]) + "/" + str(sim[1])
    print(str(n_n) + "/" + str(n_d) + " = " + sim_rs)

def sub(n1, d1, n2, d2):
    n_n = (n1*d2 - n2*d1)
    n_d = d1*d2
    sim = simpl(n_n, n_d)
    sim_rs = str(sim[0]) + "/" + str(sim[1])
    print(str(n_n) + "/" + str(n_d) + " = " + sim_rs)

def mult(n1, d1, n2, d2):
    n_n = (n1*n2)
    n_d = d1*d2
    sim = simpl(n_n, n_d)
    sim_rs = str(sim[0]) + "/" + str(sim[1])
    print(str(n_n) + "/" + str(n_d) + " = " + sim_rs)

def div(n1, d1, n2, d2):
    n_n = n1*d2
    n_d = n2*d1
    sim = simpl(n_n, n_d)
    sim_rs = str(sim[0]) + "/" + str(sim[1])
    print(str(n_n) + "/" + str(n_d) + " = " + sim_rs)



t = int(input())
for tt in range(0, t):
    # 1 / 2 + 3 / 4
    expression = input().split(' ')
    n1, d1 = int(expression[0]), int(expression[2])
    operation = expression[3]
    n2, d2 = int(expression[4]), int(expression[6])

    if (operation == '+'):
        sum(n1, d1, n2, d2)
    if (operation == '-'):
        sub(n1, d1, n2, d2)
    if (operation == '*'):
        mult(n1, d1, n2, d2)
    if (operation == '/'):
        div(n1, d1, n2, d2)
