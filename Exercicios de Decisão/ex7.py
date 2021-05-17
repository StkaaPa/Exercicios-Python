# -*- coding: utf-8 -*-

n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))


def maior():

    if n1 > n2 and n1 > n3:
        print("O maior é", n1)
    elif n2 > n1 and n2 > n3:
        print("O maior é", n2)
    elif n3 > n1 and n3 > n2:
        print("O maior é", n3)


def menor():
    if n1 < n2 and n1 < n3:
        print("O menor é", n1)
    elif n2 < n1 and n2 < n3:
        print("O menor é", n2)
    elif n3 < n1 and n3 < n2:
        print("O menor é", n3)


maior()
menor()
