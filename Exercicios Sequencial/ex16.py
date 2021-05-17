# -*- coding: utf-8 -*-

metros = float(
    input("Digite o número de metros quadrados que tem que pintar: "))
litros = int(metros/3)
print("O número de litros necessários para pintar o que necessita é de",
      litros, "litros.")
latas = int(litros/18)
preco_latas = round(latas + 0.5) * 50.00
if litros <= 18:
    print("Como são precisos menos de 18 litros para pintar, só irá precisar de comprar uma lata com o custo de 50 R$.")
else:
    print("Para pintar a área pretendida você precisa de comprar", round(latas + 0.5),
          "latas, as quais vão lhe custar um total de", preco_latas, "R$.")
