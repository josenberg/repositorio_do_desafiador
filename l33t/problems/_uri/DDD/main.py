#!/usr/bin/env python

ddd = int(input())

hash_map = {}
hash_map[61] = 'Brasilia'
hash_map[71] = 'Salvador'
hash_map[11] = 'Sao Paulo'
hash_map[21] = 'Rio de Janeiro'
hash_map[32] = 'Juiz de Fora'
hash_map[19] = 'Campinas'
hash_map[27] = 'Vitoria'
hash_map[31] = 'Belo Horizonte'

if (ddd in hash_map):
    print(hash_map[ddd])
else:
    print('DDD nao cadastrado')
