metros = float(
    input("Digite o número de metros quadrados que tem que pintar: "))
litros = float(metros/6)
print("O número de litros necessários para pintar o que necessita é de",
      litros, "litros.")

latas = int(litros/18)
resto_lata = float(litros-18)
galoes = int(litros/3.6)
resto_galoes = float(litros - 3.6)


# quantidade de latas para mistura
mistura_lata = int(litros/18)
# quantidade de galoes para mistura
mistura_galoes = int(litros - (mistura_lata * 18))/3.6

total_mistura = mistura_lata + mistura_galoes

preco_latas = round(latas + 0.5) * 80
preco_galoes = round(galoes + 0.5) * 25

preco_mistura = int((mistura_lata * 80) + (mistura_galoes * 25))

if round(litros + 0.5) <= 18:
    print("Como são precisos menos de 18 litros para pintar, só irá precisar de comprar uma lata com o custo de 80R$ e sobram-lhe", resto_lata, "litros.")
else:
    print("Para pintar a área pretendida você precisa de comprar", round(latas + 0.5),
          "latas, as quais vão lhe custar um total de", preco_latas, "R$.")

if litros <= 3.6:
    print("Como são precisos menos de 3.6 litros para pintar, só irá precisar de comprar um galão com o custo de 25R$ e sobram-lhe", resto_galoes, "litros.")
else:
    print("Para pintar a área pretendida você precisa de comprar", round(galoes + 0.5),
          "galões, as quais vão lhe custar um total de", preco_galoes, "R$.")

print("Se quiser levar mistura para poupar dinheiro terá que levar", mistura_lata,
      "latas e", round(mistura_galoes + 0.5), "galoes, e tudo isto lhe irá ficar por", preco_mistura, "R$.")
