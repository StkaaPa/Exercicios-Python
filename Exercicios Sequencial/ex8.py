# -*- coding: utf-8 -*-
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("QUANTO GANHA POR HORA?")
num = float(input("Introduza o valor de quanto ganha por hora: "))
num2 = float(input("Quantas horas trabalha por mês: "))
mes = int(input("Introduz o número de dias que trabalhou: "))
total = (num * num2) * mes
if total >= 1000:
    print("Recebe um salário acima da média, o qual é de", total, "euros.")
else:
    print("O valor do seu salário no referido mês é de", total, "euros.")
