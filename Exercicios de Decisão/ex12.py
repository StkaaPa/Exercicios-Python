# h - valor monetario por cada hora de trabalho
# t - total de horas feitas ao fim do mês

h = float(input("Digite o valor de quanto ganha por hora: "))
t = float(input("Digite o número de horas feitas ao fim do mês: "))
salbruto = h * t

IR = 0
IR2 = salbruto * 0.05
IR3 = salbruto * 0.10
IR4 = salbruto * 0.20

INSS = salbruto * 0.10
FGTS = salbruto * 0.11

totaldescontos = IR + INSS
totaldescontos2 = IR2 + INSS
totaldescontos3 = IR3 + INSS
totaldescontos4 = IR4 + INSS

saliquido = salbruto - totaldescontos
saliquido2 = salbruto - totaldescontos2
saliquido3 = salbruto - totaldescontos3
saliquido4 = salbruto - totaldescontos4

if salbruto <= 900.00:
    print("| Salario bruto: (", h * t, ") :R$", salbruto)
    print("| (-) IR (Isento) :R$", IR)
    print("| (-) INSS (10%) :R$", INSS)
    print("| (-) FGTS (11%) :R$", FGTS)
    print("| Total desdontos :R$", totaldescontos)
    print("| Salário Líquido :R$", saliquido)

if 900.00 < salbruto <= 1500.00:
    print("| Salario bruto: (", h * t, ") :R$", salbruto)
    print("| (-) IR (5%) :R$", IR2)
    print("| (-) INSS (10%) :R$", INSS)
    print("| (-) FGTS (11%) :R$", FGTS)
    print("| Total desdontos :R$", totaldescontos2)
    print("| Salário Líquido :R$", saliquido2)

if 1500.00 < salbruto <= 2500.00:
    print("| Salario bruto: (", h * t, ") :R$", salbruto)
    print("| (-) IR (10%) :R$", IR3)
    print("| (-) INSS (10%) :R$", INSS)
    print("| (-) FGTS (11%) :R$", FGTS)
    print("| Total desdontos :R$", totaldescontos3)
    print("| Salário Líquido :R$", saliquido3)

if 2500.00 < salbruto:
    print("| Salario bruto: (", h * t, ") :R$", salbruto)
    print("| (-) IR (20%) :R$", IR4)
    print("| (-) INSS (10%) :R$", INSS)
    print("| (-) FGTS (11%) :R$", FGTS)
    print("| Total desdontos :R$", totaldescontos4)
    print("| Salário Líquido :R$", saliquido4)

else:
    print("Não introduziu um valor válido!!!")
