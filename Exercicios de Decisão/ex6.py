# -*- coding: utf-8 -*-

num = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num > num2 and num > num3:
    print("O maior número é", num)
elif num2 > num and num2 > num3:
    print("O número maior é", num2)
elif num3 > num2 and num3 > num:
    print("O maior número é", num3)
