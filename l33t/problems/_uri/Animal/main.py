#!/usr/bin/env python

w1 = input()
w2 = input()
w3 = input()

enci = {
    'vertebrado-ave-carnivoro': 'aguia',
    'vertebrado-ave-onivoro': 'pomba',
    'vertebrado-mamifero-onivoro': 'homem',
    'vertebrado-mamifero-herbivoro': 'vaca',
    'invertebrado-inseto-hematofago': 'pulga',
    'invertebrado-inseto-herbivoro': 'lagarta',
    'invertebrado-anelideo-hematofago': 'sanguessuga',
    'invertebrado-anelideo-onivoro': 'minhoca',
}

print(enci[w1 + '-' + w2 + '-' + w3])
