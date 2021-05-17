# -*- coding:utf8 -*-

print("Calcular o seu peso ideal")
s = str(input("Digite o seu sexo: "))  # m para masculino e f para feminino
altura = float(input("Digite a sua altura: "))
peso = (72.7 * altura) - 58
peso2 = (62.1*altura) - 44.7
if s == "m":
    print("O seu peso ideal em relação à sua altura é de", peso, "Kg.")
elif s == "f":
    print("O seu peso ideal em relação à sua altura é de", peso2, "Kg.")
