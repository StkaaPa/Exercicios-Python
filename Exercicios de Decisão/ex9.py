# -*- coding: utf-8 -*-
print("-----Numeros Decrescente-----")
num = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num > num2 and num2 > num3:
    print("Os numeros por ordem decrescente fica: ", num, num2, num3)
elif num > num3 and num3 > num2:
    print("Os numeros por ordem decrescente fica: ", num, num3, num2)
elif num2 > num and num > num3:
    print("Os numeros por ordem decrescente fica: ", num2, num, num3)
elif num2 > num3 and num3 > num:
    print("Os numeros por ordem decrescente fica: ", num2, num3, num)
elif num3 > num and num > num2:
    print("Os numeros por ordem decrescente fica: ", num3, num, num2)
elif num3 > num2 and num2 > num:
    print("Os numeros por ordem decrescente fica: ", num3, num2, num)
elif num == num2 == num3:
    print("Os números são todos iguais")
