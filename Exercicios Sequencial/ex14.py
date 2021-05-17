# -*- coding:utf8 -*-

print("Calcular o excesso de peso e o valor da multa")
peso = float(input("Digite o valor do peixe:"))  # valor em quilos
excesso = peso - 50
print("O seu peixe tem", excesso, "Kg em excesso.")
multa = excesso * 4  # valor em euros por quilos em excesso
if peso <= 50:
    print("O peso do seu peixe é de", peso,
          "Kg, e como não tem peso em excesso não tem multa para pagar.")
elif peso > 50:
    print("Como tem peso em execesso irá ter que pagar", multa,
          "€ de multa, visto que o valor da multa é de 4€ por quilo em excesso.")
